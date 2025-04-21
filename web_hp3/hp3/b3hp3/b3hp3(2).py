from tkinter import *
def label(x,y,text):
    wd = Tk()
    wd.title("xin chào")
    wd.geometry("300x300+"+str(x)+"+"+str(y))
    label = Label(wd,text = text)
    label.pack()
    wd.mainloop()
for i in range(2):
    label(300,300,"máy bạn đã bị nhiễm virus")