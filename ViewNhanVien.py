import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkcalendar import DateEntry #pip install tkcalendar

class ViewNhanVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("QUẢN LÝ NHÂN VIÊN")
        self.geometry("1150x500")

        tk.Label(self, text="QUẢN LÝ NHÂN VIÊN", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=80, y=35)

        tk.Label(self, text="Mã Nhân Viên:").place(x=50, y=100)
        self.ma_nv = tk.Entry(self)
        self.ma_nv.place(x=200, y=100)

        tk.Label(self, text="Họ Tên:").place(x=50, y=130)
        self.ho_ten = tk.Entry(self)
        self.ho_ten.place(x=200, y=130)

        tk.Label(self, text="Lương Cơ Bản:").place(x=50, y=160)
        self.luong_cb = tk.Entry(self)
        self.luong_cb.place(x=200, y=160)

        tk.Label(self, text="Loại nhân viên:").place(x=50, y=190)
        self.nv_van_phong = tk.BooleanVar()
        tk.Checkbutton(self, text="Nhân viên văn phòng", variable=self.nv_van_phong).place(x=195, y=190)

        self.nv_ban_hang = tk.BooleanVar()
        tk.Checkbutton(self, text="Nhân viên bán hàng", variable=self.nv_ban_hang).place(x=195, y=220)

        tk.Label(self, text="Lương Hằng Tháng:").place(x=50, y=250)
        self.luong_ht = tk.Entry(self, state='readonly')
        self.luong_ht.place(x=200, y=250)

        self.tv_nhan_vien = ttk.Treeview(self,
                                         show="headings",
                                         height=20,
                                         padding="10px")
        self.tv_nhan_vien.place(x=350, y=20)
        self.tv_nhan_vien['columns'] = ('STT', 'MaNV', 'HoTen', 'LuongCB', 'LuongThang')
        self.tv_nhan_vien.column("STT", width=50, anchor='center')
        self.tv_nhan_vien.column("MaNV", width=100, anchor='e')
        self.tv_nhan_vien.column("HoTen", width=200, anchor='e')
        self.tv_nhan_vien.column("LuongCB", width=200, anchor='e')
        self.tv_nhan_vien.column("LuongThang", width=200, anchor='e')

        #self.treeview.heading('#0', text='', anchor=tk.CENTER)
        self.tv_nhan_vien.heading("STT", text="STT")
        self.tv_nhan_vien.heading("MaNV", text="Mã Nhân Viên")
        self.tv_nhan_vien.heading("HoTen", text="Họ Tên")
        self.tv_nhan_vien.heading("LuongCB", text="Lương Cơ Bản")
        self.tv_nhan_vien.heading("LuongThang", text="Lương Hàng Tháng")

        #self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        # Buttons
        self.tim_kiem = tk.Button(self, text="Tìm kiếm",
                                  width=8,
                                  background='#CCFFFF')

        self.tim_kiem.place(x=140, y=310)

        self.them_nhan_vien = tk.Button(self, text="Thêm", width=8)
        self.them_nhan_vien.place(x=50, y=350)

        self.xoa_nhan_vien = tk.Button(self, text="Xóa", width=8)
        self.xoa_nhan_vien.place(x=140, y=350)

        self.cap_nhat_nhan_vien = tk.Button(self, text="Cập nhật", width=8)
        self.cap_nhat_nhan_vien.place(x=230, y=350)

    def insert_nv(self, index, nv:list):
        nv.insert(0, index)
        self.tv_nhan_vien.insert(parent="", index=tk.END, values = nv)

    def clear_treeview(self):
        for item in self.tv_nhan_vien.get_children():
            self.tv_nhan_vien.delete(item)

if __name__ == '__main__':
    ui = ViewNhanVien()
    ui.mainloop()