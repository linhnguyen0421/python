from tkinter import *
def label(x,y,text):
    wd = Tk()
    wd.title("xin chào")
    wd.geometry("300x300+"+str(x)+"+"+str(y))
    label = Label(wd,text = text)
    label.pack()
    wd.mainloop()
label(300,300,"tên tôi là ....")