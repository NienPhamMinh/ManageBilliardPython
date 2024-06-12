import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkcalendar import *
#pip install tkcalendar

class ViewQLKH(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QUẢN LÝ KHÁCH HÀNG")
        self.geometry("1150x600")

        tk.Label(self, text="QUẢN LÝ KHÁCH HÀNG", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=50, y=35)

        tk.Label(self, text="Số điện thoại:").place(x=50, y=100)
        self.SDT = tk.Entry(self)
        self.SDT.place(x=150, y=100)

        tk.Label(self, text="Họ Tên:").place(x=50, y=130)
        self.ho_ten = tk.Entry(self)
        self.ho_ten.place(x=150, y=130)

        tk.Label(self, text="Ngày sinh:").place(x=50, y=160)
        self.ngaySinh = tk.Entry(self)
        self.ngaySinh.place(x=150, y=160)
        self.ngaySinh.insert(0,"dd/mm/yyyy")
        self.ngaySinh.bind("<1>",self.goiNgay)

        self.tv_khach_hang = ttk.Treeview(self,
                                         show="headings",
                                         height=25,
                                         padding="11px")
        self.tv_khach_hang.place(x=320, y=20)
        self.tv_khach_hang['columns'] = ('STT', 'sdt', 'HoTen', 'NgaySinh')
        self.tv_khach_hang.column("STT", width=40, anchor='center')
        self.tv_khach_hang.column("sdt", width=300, anchor='e')
        self.tv_khach_hang.column("HoTen", width=210, anchor='e')
        self.tv_khach_hang.column("NgaySinh", width=210, anchor='e')


        # self.treeview.heading('#0', text='', anchor=tk.CENTER)
        self.tv_khach_hang.heading("STT", text="STT")
        self.tv_khach_hang.heading("sdt", text="Số Điện Thoại")
        self.tv_khach_hang.heading("HoTen", text="Họ Tên")
        self.tv_khach_hang.heading("NgaySinh", text="Ngày Sinh")


        #self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        # Buttons
        self.tim_kiem = tk.Button(self, text="Tìm kiếm",
                                  width=8,
                                  background='#CCFFFF')

        self.tim_kiem.place(x=140, y=250)

        self.them_khach_hang = tk.Button(self, text="Thêm", width=8)
        self.them_khach_hang.place(x=50, y=200)

        self.xoa_khach_hang = tk.Button(self, text="Xóa", width=8)
        self.xoa_khach_hang.place(x=140, y=200)

        self.cap_nhat_khach_hang = tk.Button(self, text="Cập nhật", width=8)
        self.cap_nhat_khach_hang.place(x=230, y=200)

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
    def grab_date(self):
        self.ngaySinh.delete(0,tk.END)
        self.ngaySinh.insert(0,cal.get_date())
        # tk.delete_window.destroyt()



    def insert_kh(self, index, kh:list): #  thêm dữ liệu vào treeview
        kh.insert(0, index)
        self.tv_khach_hang.insert(parent="", index=tk.END, values = kh)

    def clear_treeview(self): #  xóa dữ liệu vào treeview
        for item in self.tv_khach_hang.get_children():
            self.tv_khach_hang.delete(item)

if __name__ == '__main__':
    ui = ViewQLKH()
    list1=[['0907234123','nien','28-08-1997'],['09072343243','nguyen','28-08-2001']]
    for i in range(len(list1)):
        ui.insert_kh(i,list1[i])
    ui.mainloop()