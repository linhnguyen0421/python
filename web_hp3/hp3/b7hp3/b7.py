from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

        # entry
        self.nhap1 = StringVar()
        self.en1 = ttk.Entry(self.cs, font="Arial 15", width=10, textvariable=self.nhap1)
        self.en1.grid(row=0, column=1, padx=10)

        self.nhap2 = StringVar()
        self.en2 = ttk.Entry(self.cs, font="Arial 15", width=10, textvariable=self.nhap2, show="*")
        self.en2.grid(row=1, column=1, padx=10)

        # button
        self.btn1 = Button(self.cs, text="Đăng nhập", command=self.dang_nhap)
        self.btn1.grid(row=2, column=0, columnspan=2, pady=10)

    def dang_nhap(self):
        # Xử lý đăng nhập ở đây nếu cần
        username = self.en1.get()
        password = self.en2.get()

        # Kiểm tra tài khoản và mật khẩu (đơn giản)
        if username == "tien" and password == "1":
            messagebox.showinfo("thông báo:","bạn đã đăng nhập thành công.")
            self.cs.destroy()
            menu_window = menu()
            menu_window.run()

        else:
            messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng.")
class menu:
    def __init__(self):
        self.cs = Tk()
        self.cs.title("phần mềm quản lý")
        self.cs.geometry("320x175")
    def open_file():
        messagebox.showinfo("Open", "Opening a file...")

    def save_file():
        messagebox.showinfo("Save", "Saving the file...")

    def cut_text():
        messagebox.showinfo("Cut", "Cutting text...")

    def copy_text():
        messagebox.showinfo("Copy", "Copying text...")

    def paste_text():
        messagebox.showinfo("Paste", "Pasting text...")

    def about():
        messagebox.showinfo("About", "This is a simple Tkinter menu example.")
    
    def run(self):

        window = self.cs
        window.title("Tkinter Menu Example")

        # Tạo thanh công cụ menu
        menu_bar = Menu(window)
        window.config(menu=menu_bar)

        # tạo file menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=menu.open_file)
        file_menu.add_command(label="Save", command=menu.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)

        # tạo phần edit menu
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=menu.cut_text)
        edit_menu.add_command(label="Copy", command=menu.copy_text)
        edit_menu.add_command(label="Paste", command=menu.paste_text)

        # tạo phần help menu
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=menu.about)

if __name__ == "__main__":
    a = CuasoDangNhap()
