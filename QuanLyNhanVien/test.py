from M_QLNV import ModelQLNV
from V_QLNV import ViewQLNV
from C_QLNV import ControlQLNV


if __name__ == '__main__':
    view = ViewQLNV()
    model = ModelQLNV()
    control = ControlQLNV(view, model)
    control.insertTreeView()
    control.addNhanVien()
    control.Update_WorkDay_NhanVien()
    control.DeleteNhanVien()
    control.tinhLuong()
    view.mainloop()