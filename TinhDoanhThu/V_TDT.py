import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from tkinter import  messagebox
from tkcalendar import DateEntry #pip install tkcalendar
from datetime import  datetime
import locale

class View_TDT(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TÍNH DOANH THU")
        self.geometry("1250x700")

        tk.Label(self, text="DOANH THU", fg='RED',
                 font=tkFont.Font(family="Helvetica", size=12, weight="bold")
                ).place(x=50, y=75)

        self.tv_doanh_thu = ttk.Treeview(self,
                                         show="headings",
                                         height=30,
                                         padding="10px")
        self.tv_doanh_thu.place(x=400, y=20)
        self.tv_doanh_thu['columns'] = ('STT', 'Ngay', 'DoanhThu')
        self.tv_doanh_thu.column("STT", width=50, anchor='center')
        self.tv_doanh_thu.column("Ngay", width=300, anchor='e')
        self.tv_doanh_thu.column("DoanhThu", width=300, anchor='e')

        #self.treeview.heading('#0', text='', anchor=tk.CENTER)
        self.tv_doanh_thu.heading("STT", text="STT")
        self.tv_doanh_thu.heading("Ngay", text="Ngày tháng năm")
        self.tv_doanh_thu.heading("DoanhThu", text="Doanh Thu")

        #self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        # Buttons


        self.doanh_thu = tk.Button(self, text="Tổng danh thu", width=12)
        self.doanh_thu.place(x=50, y=150)

        self.chi_phi = tk.Button(self, text="Chi phí", width=12)
        self.chi_phi.place(x=160, y=150)

        self.loi_nhuan = tk.Button(self, text="Lợi nhuận", width=12)
        self.loi_nhuan.place(x=270, y=150)

    def insert_dt(self, index, nv:list):
        nv.insert(0, index)
        self.tv_doanh_thu.insert(parent="", index=tk.END, values = nv)

    def clear_treeview(self):
        for item in self.tv_doanh_thu.get_children():
            self.tv_doanh_thu.delete(item)
    # pop-up doanh thu
    def DoanhThuThang(self,DoanhThu):
        locale.setlocale(locale.LC_ALL,'')
        formatDT = locale.format_string("%d",DoanhThu,grouping=True)
        month = datetime.now().month
        box= tk.Toplevel()
        box.geometry("550x550")
        box.title("Doanh thu tháng {}".format(month))
        label = tk.Label(box,text="Tổng doanh thu : {} đồng ".format(formatDT),font=tkFont.Font(family="Helvetica", size=18, weight="bold")).place(x=50,y=50)
    # pop up chi phí
    def ChiPhi(self,luongNV):
        locale.setlocale(locale.LC_ALL, '')
        formatLuong = locale.format_string("%d", luongNV, grouping=True)
        month = datetime.now().month
        box= tk.Toplevel()
        box.geometry("550x550")
        box.title("Chi phí tháng {}".format(month))
        label = tk.Label(box,text="Tổng lương nhân viên : {} đồng ".format(formatLuong),font=tkFont.Font(family="Helvetica", size=18, weight="bold")).place(x=50,y=50)
    # pop up lợi nhuận
    def LoiNhuan(self,loiNhuan):
        locale.setlocale(locale.LC_ALL, '')
        formatLN = locale.format_string("%d", loiNhuan, grouping=True)
        month = datetime.now().month
        box= tk.Toplevel()
        box.geometry("550x550")
        box.title("Lợi nhuận tháng {}".format(month))
        label = tk.Label(box,text="Lợi nhuận : {} đồng ".format(formatLN),font=tkFont.Font(family="Helvetica", size=18, weight="bold")).place(x=50,y=50)
if __name__ == '__main__':
    ui = View_TDT()

    ui.mainloop()