import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import messagebox
from tkcalendar import DateEntry #pip install tkcalendar

class ViewDN(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ĐĂNG NHẬP")
        self.geometry("400x400")

        tk.Label(self, text="ĐĂNG NHẬP", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=50, y=35)


        self.quan_ly = tk.BooleanVar()
        tk.Checkbutton(self, text="Quán lý", variable=self.quan_ly).place(x=50, y=100)

        self.nhan_vien = tk.BooleanVar()
        tk.Checkbutton(self, text="Nhân viên", variable=self.nhan_vien).place(x=150, y=100)


        tk.Label(self, text="Mã đăng nhập:").place(x=50, y=130)
        self.ten_dang_nhap = tk.Entry(self)
        self.ten_dang_nhap.place(x=200, y=130)

        tk.Label(self, text="Password:").place(x=50, y=160)
        self.password = tk.Entry(self,show="*")
        self.password.place(x=200, y=160)


        # Buttons

        self.dang_nhap = tk.Button(self, text="Login", width=10, background='#94FB88',command= self.show_message)
        self.dang_nhap.place(x=50, y=200)

        self.huy = tk.Button(self, text="Cancel", width=10, background='#FB9C88')
        self.huy.place(x=140, y=200)

    # pop up thông báo
    def DangNhapThanhCong(self):
        return messagebox.showinfo(title='Login Status',message="Đăng nhập thành công")
    def DangNhapKhongThanhCong(self):
        return messagebox.showerror(title='Login Error',message="Tên đăng nhâp/ Password chưa đúng")
    def ThongBaoChon(self):
        return messagebox.showerror(title='Login Error',message="Bạn chươ chọn chức vụ")

    def show_message(self):
        if self.quan_ly.get():
            print(self.ten_dang_nhap.get())




if __name__ == '__main__':
    ui = ViewDN()
    print(ui.quan_ly.get())

    ui.mainloop()