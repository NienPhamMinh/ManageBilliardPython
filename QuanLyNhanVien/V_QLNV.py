import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkcalendar import *
#pip install tkcalendar

class ViewQLNV(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QUẢN LÝ NHÂN VIÊN")
        self.geometry("1150x600")

        tk.Label(self, text="QUẢN LÝ NHÂN VIÊN", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=50, y=35)

        tk.Label(self, text="Mã nhân viên:").place(x=50, y=100)
        self.id = tk.Entry(self)
        self.id.place(x=150, y=100)

        tk.Label(self, text="Họ tên:").place(x=50, y=130)
        self.ho_ten = tk.Entry(self)
        self.ho_ten.place(x=150, y=130)

        tk.Label(self, text="Mật khẩu:").place(x=50, y=160)
        self.password = tk.Entry(self)
        self.password.place(x=150, y=160)

        tk.Label(self, text="Ngày làm việc:").place(x=50, y=190)
        self.wd = tk.Entry(self)
        self.wd.place(x=150, y=190)






        self.tv_nhan_vien = ttk.Treeview(self,
                                         show="headings",
                                         height=25,
                                         padding="11px")
        self.tv_nhan_vien.place(x=320, y=20)
        self.tv_nhan_vien['columns'] = ('STT', 'manv', 'HoTen', 'matKhau','NgayLamViec','luong')
        self.tv_nhan_vien.column("STT", width=30, anchor='center')
        self.tv_nhan_vien.column("manv", width=50, anchor='e')
        self.tv_nhan_vien.column("HoTen", width=200, anchor='e')
        self.tv_nhan_vien.column("matKhau", width=150, anchor='e')
        self.tv_nhan_vien.column("NgayLamViec", width=150, anchor='e')
        self.tv_nhan_vien.column("luong", width=200, anchor='e')


        # self.treeview.heading('#0', text='', anchor=tk.CENTER)
        self.tv_nhan_vien.heading("STT", text="STT")
        self.tv_nhan_vien.heading("manv", text="Mã NV")
        self.tv_nhan_vien.heading("HoTen", text="Họ Tên")
        self.tv_nhan_vien.heading("matKhau", text="Mật Khẩu")
        self.tv_nhan_vien.heading("NgayLamViec", text="Ngày Làm Việc")
        self.tv_nhan_vien.heading("luong", text="Lương")


        #self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        # Buttons
        self.tinh_luong = tk.Button(self, text="Tính lương",
                                  width=9,
                                  background='#CCFFFF')

        self.tinh_luong.place(x=135, y=280)

        self.them_nhan_vien = tk.Button(self, text="Thêm", width=8)
        self.them_nhan_vien.place(x=50, y=230)

        self.xoa_nhan_vien = tk.Button(self, text="Xóa", width=8)
        self.xoa_nhan_vien.place(x=140, y=230)

        self.cap_nhat_nhan_vien = tk.Button(self, text="Cập nhật", width=8)
        self.cap_nhat_nhan_vien.place(x=230, y=230)

    #chon ngay
    def goiNgay(self,event):
        global cal
        date_window = tk.Toplevel()
        date_window.grab_set()
        date_window.title('Chọn ngày sinh:')
        date_window.geometry('250x220+590+370')
        cal = Calendar(date_window,selectmode="day",date_pattern="dd-mm-y")
        cal.place(x=0,y=0)

        submit = tk.Button(date_window,text= "Nhận", command=self.grab_date)
        submit.place(x=80,y=190)
    # def grab_date(self):
    #     self.ngaySinh.delete(0,tk.END)
    #     self.ngaySinh.insert(0,cal.get_date())
    #     # tk.delete_window.destroyt()



    def insert_kh(self, index, kh:list):
        kh.insert(0, index)
        self.tv_nhan_vien.insert(parent="", index=tk.END, values = kh)

    def clear_treeview(self):
        for item in self.tv_nhan_vien.get_children():
            self.tv_nhan_vien.delete(item)

if __name__ == '__main__':
    ui = ViewQLNV()
    list1=[['0907234123','nien','28-08-1997'],['09072343243','nguyen','28-08-2001']]
    for i in range(len(list1)):
        ui.insert_kh(i,list1[i])
    ui.mainloop()