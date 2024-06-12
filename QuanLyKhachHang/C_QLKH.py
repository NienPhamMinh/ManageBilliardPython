from M_QLKH import ModelQLKH
from V_QLKH import ViewQLKH


class ControlQLKH:
    def __init__(self, view:ViewQLKH, model:ModelQLKH):
        self.view = view
        self.model = model
        self.view.them_khach_hang.config(command=self.addKhachHang)
        self.view.xoa_khach_hang.config(command=self.deleteKhachHang)
        self.view.cap_nhat_khach_hang.config(command=self.UpdateKhachHang)
        self.view.tim_kiem.config(command=self.FindKhachHang)
    # dữ liệu từ mysql trả về là 1 tuple mà tuple không chỉnh sửa được trong treeview nên
    # em đổi sang kiểu list
    def insertTreeView(self):
        tupleKH = self.model.loadKH()

        listKH =[]
        # chuyển tuple thành list
        for i in range(len(tupleKH)):
            j = list(tupleKH[i])
            listKH.append(j)

        for i in range(len(listKH)):
            self.view.insert_kh(i+1,listKH[i])
    # Thêm 1 kết quả duy nhất fetchone vào treeview
    def insertResult(self,tupleResult):
        # self.view.clear_treeview()
        listResult = list(tupleResult)
        self.view.insert_kh(1,listResult)
    def addKhachHang(self):
        if self.view.SDT.get() and self.view.ho_ten.get() and self.view.ngaySinh.get():
            phone = self.view.SDT.get()
            name = self.view.ho_ten.get()
            dob = self.view.ngaySinh.get()
            self.model.insert_KH(phone,name,dob)
        self.view.clear_treeview()
        self.insertTreeView()

    def deleteKhachHang(self):
        if self.view.SDT.get():
            phone = self.view.SDT.get()
            self.model.delete_KH(phone)
        self.view.clear_treeview()
        self.insertTreeView()

    def UpdateKhachHang(self):
        name = self.view.ho_ten.get()
        phone = self.view.SDT.get()
        self.model.update_name_KH(name,phone)
        self.view.clear_treeview()
        self.insertTreeView()

    def FindKhachHang(self):
        phone = self.view.SDT.get()
        if self.model.find_KH(phone) is not None:
            self.view.clear_treeview()
            # return self.model.find_KH(phone)
            self.insertResult(self.model.find_KH(phone))


if __name__ == '__main__':
    view = ViewQLKH()
    model = ModelQLKH()
    control = ControlQLKH(view, model)
    control.insertTreeView()
    control.addKhachHang()
    control.UpdateKhachHang()

    view.mainloop()
