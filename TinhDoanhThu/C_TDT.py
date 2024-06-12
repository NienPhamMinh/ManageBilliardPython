from M_TDT import Model_TDT
from  V_TDT import View_TDT


class Control_TDT:
    def __init__(self,view:View_TDT,model:Model_TDT):
        self.view = view
        self.model = model
        self.view.doanh_thu.config(command=self.TongDT)
        self.view.chi_phi.config(command=self.LuongNV)
        self.view.loi_nhuan.config(command=self.LoiNHuan)
    def insertTreeView(self):
        tupleDT = self.model.LoadDoanhThu()

        listDT = []
        # chuyển tuple thành list
        for i in range(len(tupleDT)):
            j = list(tupleDT[i])
            listDT.append(j)

        for i in range(len(listDT)):
            self.view.insert_dt(i + 1, listDT[i])

    def TongDT(self):
        tongDT = self.model.DoanhThuThang()
        self.view.DoanhThuThang(round(tongDT[0][0],0))

    def LuongNV(self):
        luongNV = self.model.TongLuong()
        self.view.ChiPhi(round(luongNV[0][0],0))

    def LoiNHuan(self):
        doanhThu = self.model.DoanhThuThang()
        chiPhi = self.model.TongLuong()
        loiNhuan = doanhThu[0][0] - chiPhi[0][0]
        self.view.LoiNhuan(round(loiNhuan,0))



if __name__ == '__main__':
    model = Model_TDT()
    view = View_TDT()
    control = Control_TDT(view,model)
    control.insertTreeView()

    view.mainloop()