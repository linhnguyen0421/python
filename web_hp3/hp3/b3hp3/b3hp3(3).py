from tkinter import *
from tkinter import ttk
def label(x,y,text):
    wd = Tk()
    wd.title("xin chào")
    wd.geometry("300x300+"+str(x)+"+"+str(y))
    label = Label(wd,text = text)
    label.pack()
    wd.mainloop()
def entry(self):
    self.nhap1 = StringVar()
    self.en1 = ttk.Entry(self.cs, font="Arial 15", width=10, textvariable=self.nhap1)
    self.en1.grid(row=0, column=1, padx=10)

    self.nhap2 = StringVar()
    self.en2 = ttk.Entry(self.cs, font="Arial 15", width=10, textvariable=self.nhap2, show="*")
    self.en2.grid(row=1, column=1, padx=10)
    self.mainloop()
label(300,300,"xin chào")

