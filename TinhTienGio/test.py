from  C_TTG import ControlTTG
from M_TTG import ModelTTG
from  V__TTG import ViewTTG

if __name__ == '__main__':
    view = ViewTTG()
    model = ModelTTG()
    control = ControlTTG(model, view)
    control.insertTreeView()

    view.mainloop()