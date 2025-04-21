from tkinter import *
window=Tk()
window.title("Linn")
window.geometry('300x300+300+200')
linn1=Label(window,text="Teky xin chào",bg="blue",fg="pink",font="Times 32")
linn1.pack(side="bottom")
linn2=Label(window,text="Tôi tên là :Phạm Gia Khiêm"
            ,bd=1,relief='solid',justify=RIGHT,width=30,height=15,anchor=SE)
linn2.pack()
window.mainloop()