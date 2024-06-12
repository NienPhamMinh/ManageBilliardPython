from C_QLKH import  ControlQLKH
from M_QLKH import ModelQLKH
from  V_QLKH import ViewQLKH


if __name__ == '__main__':
    view = ViewQLKH()
    model = ModelQLKH()
    control = ControlQLKH(view,model)
    control.insertTreeView()
    # control.addKhachHang()
    # control.UpdateKhachHang()
    # control.deleteKhachHang()
    if control.view.tim_kiem.bind:
        result = control.FindKhachHang()




    view.mainloop()