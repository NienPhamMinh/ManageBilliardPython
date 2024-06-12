from C_DN import ControlDN
from V_DN import ViewDN
from M_DN import ModelDN
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import messagebox
from tkinter import messagebox
if __name__ == '__main__':
    view = ViewDN()
    model = ModelDN()
    # self.view.dang_nhap.config(command=self.DangNhap(self.view.ten_dang_nhap, self.view.password))
    controller = ControlDN(view,model)
    controller.DangNhap()
    view.mainloop()