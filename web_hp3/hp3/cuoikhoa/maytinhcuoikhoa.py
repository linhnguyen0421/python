import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Máy Tính Cầm Tay")

        # Entry để hiển thị các số và kết quả
        self.display_var = tk.StringVar()
        entry = ttk.Entry(master, textvariable=self.display_var, font=('Arial', 14), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Các nút cho các số và toán tử
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'sqrt', 'fact'
        ]

        # Thiết lập các nút trên lưới
        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(master, text=button, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew', ipadx=10, ipady=10)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def clear_entry(self):
        self.display_var.set("")

    def on_button_click(self, button):
        current_text = self.display_var.get()

        if button == 'C':
            self.clear_entry()
        elif button == 'sqrt':
            try:
                result = math.sqrt(float(current_text))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Lỗi")
        elif button == 'fact':
            try:
                result = str(math.factorial(int(current_text)))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Lỗi")
        elif button == '=':
            try:
                result = str(eval(current_text))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Lỗi")
        else:
            new_text = current_text + button
            self.display_var.set(new_text)

    def run(self):
        self.master.mainloop()

class LoginWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("300x150")

        self.label_username = tk.Label(root, text="Tài khoản:")
        self.label_password = tk.Label(root, text="Mật khẩu:")

        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        self.label_username.grid(row=0, column=0)
        self.label_password.grid(row=1, column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.login_button = tk.Button(root, text="Đăng nhập", command=self.login)
        self.login_button.grid(row=2, column=1)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra tài khoản và mật khẩu (đơn giản)
        if username == "tien" and password == "1":
            self.root.destroy()
            calculator = tk.Tk()
            app = CalculatorApp(calculator)
            app.run()
        else:
            messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng.")

if __name__ == "__main__":
    cs = tk.Tk()
    app = LoginWindow(cs)
    cs.mainloop()
