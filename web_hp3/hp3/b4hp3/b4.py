from tkinter import *
from tkinter import ttk

class CuasoDangNhap:
    def __init__(self):
        self.cs = Tk()
        self.cs.title("Vui lòng đăng nhập")
        self.cs.geometry("300x150")
        self.show()
        self.cs.mainloop()

    def show(self):
        # label
        self.lbl1 = Label(self.cs, text="Tên đăng nhập", bg="gray", fg="black", font="Arial 10", bd=2, relief="raised")
        self.lbl1.grid(row=0, column=0, padx=10)

        self.lbl2 = Label(self.cs, text="Mật khẩu", bg="gray", fg="black", font="Arial 10", bd=2, relief="raised")
        self.lbl2.grid(row=1, column=0, padx=10)

        # button
        self.btn1 = Button(self.cs, text="Đăng nhập", command=self.thay_doi)
        self.btn1.grid(row=2, column=0, columnspan=2, pady=10)
    def thay_doi(self):
        self.btn2 = Button(self.cs, text="chào mừng đăng nhập vào phần mềm")
        self.btn2.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    a = CuasoDangNhap()
