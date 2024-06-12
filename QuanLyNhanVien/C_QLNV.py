from M_QLNV import ModelQLNV
from V_QLNV import ViewQLNV



class ControlQLNV:
    def __init__(self, view:ViewQLNV, model:ModelQLNV):
        self.view = view
        self.model = model
        self.view.them_nhan_vien.config(command=self.addNhanVien)
        self.view.xoa_nhan_vien.config(command=self.DeleteNhanVien)
        self.view.cap_nhat_nhan_vien.config(command=self.Update_WorkDay_NhanVien)
        self.view.tinh_luong.config(command=self.tinhLuong)

    def insertTreeView(self):
        tupleKH = self.model.loadNV()

        listKH =[]
        # chuyển tuple thành list
        for i in range(len(tupleKH)):
            j = list(tupleKH[i])
            listKH.append(j)

        for i in range(len(listKH)):
            self.view.insert_kh(i+1,listKH[i])
    def insertResult(self,tupleResult):
        listResult = list(tupleResult)
        self.view.insert_kh(1,listResult)
    def addNhanVien(self):
        if self.view.id.get() and self.view.ho_ten.get() and self.view.password.get():
            id = self.view.id.get()
            name = self.view.ho_ten.get()
            password = self.view.password.get()
            password = self.view.password.get()
            self.model.insert_NV(id,name,password)
        self.view.clear_treeview()
        self.insertTreeView()

    def DeleteNhanVien(self):
        if self.view.id.get():
            id = self.view.id.get()
            self.model.delete_NV(id)
        self.view.clear_treeview()
        self.insertTreeView()
    # cập nhật ngày làm việc cho nhân viên
    def Update_WorkDay_NhanVien(self):
        id = self.view.id.get()
        wd = self.view.wd.get()
        self.model.update_workDay_NV(wd,id)
        self.view.clear_treeview()
        self.insertTreeView()

    # def FindNhanVien(self):
    #     id = self.view.id.get()
    #     print(id)
    #     if self.model.find_NV(id) is not None:
    #         self.view.clear_treeview()
    #         result = model.find_KH(id)
    #         self.insertResult(result)
    # Tính lương cho nhân viên
    def tinhLuong(self):
        id = self.view.id.get()
        self.model.update_Luong_NV(id)
        self.view.clear_treeview()
        self.insertTreeView()


if __name__ == '__main__':
    view = ViewQLNV()
    model = ModelQLNV()
    control = ControlQLNV(view,model)
    control.insertTreeView()
    control.addNhanVien()
    control.Update_WorkDay_NhanVien()
    control.DeleteNhanVien()
    control.tinhLuong()
    view.mainloop()
