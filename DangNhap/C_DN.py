from V_DN import ViewDN
from M_DN import  ModelDN
import tkinter as tk
from tkinter import messagebox
class ControlDN:
    def __init__(self, view:ViewDN, model :ModelDN):
        self.view = view
        self.model = model
        self.view.dang_nhap.config(command=self.DangNhap)

        # xử lý sự kien check ten dang nhap va pass word #
    def DangNhap(self):
        if self.view.quan_ly.get() and not self.view.nhan_vien.get():
            if self.model.DangNhap_QL(self.view.ten_dang_nhap.get(),self.view.password.get()) :
                self.view.DangNhapThanhCong()
            else:
                self.view.DangNhapKhongThanhCong()
        elif self.view.nhan_vien.get() and not self.view.quan_ly.get():
            if self.model.DangNhap_NV(self.view.ten_dang_nhap.get(),self.view.password.get()):
                self.view.DangNhapThanhCong()
            else:
                self.view.DangNhapKhongThanhCong()
        if self.view.quan_ly.get() and self.view.nhan_vien.get() :
            self.view.ThongBaoChon()





if __name__ == '__main__':
    view = ViewDN()
    model = ModelDN()
    # self.view.dang_nhap.config(command=self.DangNhap(self.view.ten_dang_nhap, self.view.password))
    controller = ControlDN(view, model)
    controller.DangNhap()
