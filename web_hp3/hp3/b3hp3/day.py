from tkinter import *
def cuaso():
    a = Tk()
    a.title("xin chào")
    a.geometry("300x300+500+500")
    lb1 = Label(a,text="chào mọi người",bg="gray", fg="black", font="Arial 10", bd=2, relief="raised")
    lb1.pack()
    bt1 = Button(a,text="đăng nhập",bg="gray", fg="black", font="Arial 10", bd=2, relief="raised")
    bt1.pack()
    a.mainloop()
cuaso()