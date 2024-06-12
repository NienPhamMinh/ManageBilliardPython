import tkinter as tk
from tkinter import ttk
window = tk.Tk()
tree = ttk.Treeview(master=window)
tree['columns']=('column1','column2','column3')
tree.heading('column1',text='cột1')
tree.heading('column2',text='cọt2')
tree.heading('column3',text='cột3')
#them du lieu
tree.insert(parent="",index=tk.END,text="Dòng 1",values=('Giá trị 1','Giá trị 2',"Giá trị 3"))

tree.pack()
window.mainloop()