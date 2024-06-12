import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import  messagebox
class ViewTTG(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TÍNH TIỀN GIỜ')
        self.geometry('1150x600')
        tk.Label(self, text="TÍNH TIỀN GIỜ", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                 ).place(x=50, y=50)

        tk.Label(self, text="Mã Bàn:",font=tkFont.Font(family="Helvetica",size=11)).place(x=50, y=100)
        self.ma_ban = tk.Entry(self)
        self.ma_ban.place(x=150, y=100)

        tk.Label(self,text="Mã nhân viên:",font=tkFont.Font(family="Helvetica",size=11)).place(x=50,y=140)
        self.ma_nv = tk.Entry(self)
        self.ma_nv.place(x=150,y=140)

        self.tv_ban = ttk.Treeview(self,
                                         show="headings",
                                         height=20,
                                         padding="10px")
        self.tv_ban.place(x=350, y=20)
        self.tv_ban['columns'] = ('STT', 'MaBan', 'CheckIn', 'CheckOut', 'MaNV','Ngay')
        self.tv_ban.column("STT", width=50, anchor='center')
        self.tv_ban.column("MaBan", width=100, anchor='e')
        self.tv_ban.column("CheckIn", width=150, anchor='e')
        self.tv_ban.column("CheckOut", width=150, anchor='e')
        self.tv_ban.column("MaNV", width=150, anchor='e')
        self.tv_ban.column("Ngay", width=150, anchor='e')

        # self.treeview.heading('#0', text='', anchor=tk.CENTER)
        self.tv_ban.heading("STT", text="STT")
        self.tv_ban.heading("MaBan", text="Mã Bàn")
        self.tv_ban.heading("CheckIn", text="Check In")
        self.tv_ban.heading("CheckOut", text="Check Out")
        self.tv_ban.heading("MaNV", text="Mã NV")
        self.tv_ban.heading("Ngay", text="Ngày")

        # self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        # Button

        self.check_in = tk.Button(self, text="CHECK IN", width=12,background='#FB9C88')
        self.check_in.place(x=50, y=180)

        self.check_out = tk.Button(self, text="CHECK OUT", width=12,background='#94FB88')
        self.check_out.place(x=170, y=180)
    # pop up tính tiền
    def TinhTien(self,id,tienGio):
        box= tk.Toplevel()
        box.geometry("250x250")
        box.title("Tính tiền giờ".format(id))
        label = tk.Label(box,text="Tiền : {} đồng ".format(tienGio),font=tkFont.Font(family="Helvetica", size=18, weight="bold")).place(x=50,y=50)

    def BanDaCheckIn(self):
        return messagebox.showinfo(title=' Thông báo  ', message=" Bàn đã check in")

    def chuaNhapMaNV(self):
        return messagebox.showinfo(title=' Thông báo  ', message=" Chưa nhập mã NV")
    def insert_ban(self, index, nv: list):
        nv.insert(0, index)
        self.tv_ban.insert(parent="", index=tk.END, values=nv)

    def clear_treeview(self):
        for item in self.tv_ban.get_children():
            self.tv_ban.delete(item)


if __name__ == '__main__':
    ui = ViewTTG()
    ui.mainloop()