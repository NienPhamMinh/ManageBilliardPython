import tkinter as tk

from tkinter import  *
root = tk.Tk()
root.geometry("1150x900")
root.title("Tinh luong nhan vien")
label = tk.Label(root,text='Tên Nhân Viên',font=('arial',18))
label.pack()
textbox = tk.Text(root,font=('airal',20),height=3)
textbox.pack()

root.mainloop()
