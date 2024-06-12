from M_TTG import  ModelTTG
from V__TTG import ViewTTG
from datetime import  datetime, timedelta
from datetime import date
import math

class ControlTTG:
    def __init__(self,model:ModelTTG,view:ViewTTG):
        self.view = view
        self.model = model
        self.view.check_in.config(command=self.checkIn)
        self.view.check_out.config(command=self.checkOut)

    def checkIn(self):
        idBan = self.view.ma_ban.get()
        idNV = self.view.ma_nv.get()
        if not self.view.ma_nv.get():
            self.view.chuaNhapMaNV() # nhân viên phải nhập mã nhân viên
        else:
            if len(self.model.checkBan(idBan,idNV))==0: # nếu mã nv và mã bàn chưa có thì tạo mới
                self.model.insert_Ban(idBan, idNV)
            else: # kiểm tra nếu bàn đã tạo giờ check out là null và giờ check in không null thông báo cho nv biết bàn đã check in
                if self.model.get_checkOut(idBan, idNV)[0] is None and self.model.get_checkIn(idBan, idNV) is not None:
                    self.view.BanDaCheckIn()
                else: # nếu bàn không check in thì tạo mới
                    self.model.insert_Ban(idBan, idNV)

        self.view.clear_treeview()
        self.insertTreeView()


    def checkOut(self):
        idBan = self.view.ma_ban.get()
        idNV = self.view.ma_nv.get()
        self.model.update_checkOUT(idBan,idNV)
        # print(type(self.model.get_checkOut(idBan,idNV)[0]))
        # lấy giờ check out và check in
        end = self.model.get_checkOut(idBan,idNV)[0]
        star = self.model.get_checkIn(idBan,idNV)[0]
        # time_end = datetime.combine(ngay.date(),end)
        # time_star = datetime.combine(ngay.date(),star)
        # 1 giờ là 50.000 đồng
        tienGio = round(((end-star).total_seconds()/3600 )* 50000,0)
        # thông báo tiền giờ cho khách hàng
        self.view.TinhTien(idBan,tienGio)
        # print(end)
        # print(star)
        # print(tienGio)
        # print(self.model.checkDoanhThu(idBan))
        self.view.clear_treeview()
        self.insertTreeView()
        # cập nhật doanh thu vào bàn
        if self.model.checkDoanhThu(idBan)[0][0] is None:
            self.model.update_DoanhThu_NUll(tienGio,idBan)
        else:
            self.model.update_DoanhThu_NOT_NUll(tienGio,idBan)

    def insertTreeView(self):
        tupleBan = self.model.loadBan()

        listBan =[]
        # chuyển tuple thành list
        for i in range(len(tupleBan)):
            j = list(tupleBan[i])
            listBan.append(j)

        for i in range(len(listBan)):
            self.view.insert_ban(i+1,listBan[i])



if __name__ == '__main__':
    view = ViewTTG()
    model = ModelTTG()
    control = ControlTTG(model,view)
    control.insertTreeView()


    view.mainloop()

