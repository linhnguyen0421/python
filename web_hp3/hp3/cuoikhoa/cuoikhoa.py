import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RegisterWindow:
    def __init__(self, root, registered_accounts, login_callback):
        self.root = root
        root.title('Paint app')

        self.label = tk.Label(root, text='Welcome to paint web', fg='blue')
        self.label.pack()

        self.label1 = tk.Label(root, text='( •̀ ω •́ )✧', fg='black')
        self.label1.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack()

        self.registered_accounts = registered_accounts
        self.login_callback = login_callback

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Kiểm tra xem tài khoản đã tồn tại hay chưa
        if any(user == username for user, _ in self.registered_accounts):
            messagebox.showerror("Lỗi ", "tài khoản không tồn tại.")
            return

        # Ghi tên người dùng và mật khẩu vào tệp
        with open("user.txt", "a") as file:
            file.write(f"{username},{password}\n")

        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

        messagebox.showinfo("Tạo tài khoản", "Đã tạo tài khoản thành công, giờ hãy đăng nhập")
        
        # Tự động mở cửa sổ đăng nhập sau khi đăng ký
        self.login_callback()


class LoginWindow:
    def __init__(self, root, registered_accounts, home_callback):
        self.root = root
        self.root.title("Login")

        self.label_username = tk.Label(root, text="Username:")
        self.label_password = tk.Label(root, text="Password:")

        self.entry_username = ttk.Entry(root)
        self.entry_password = ttk.Entry(root, show="*")

        self.label_username.grid(row=0, column=0, pady=10)
        self.label_password.grid(row=1, column=0, pady=10)
        self.entry_username.grid(row=0, column=1, pady=10)
        self.entry_password.grid(row=1, column=1, pady=10)

        self.login_button = ttk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.registered_accounts = registered_accounts
        self.home_callback = home_callback

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Kiểm tra tên người dùng và mật khẩu với dữ liệu từ tệp "user.txt"
        with open("user.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Login", "Login successful.")
                    self.root.destroy()  
                    self.home_callback()  
                    return
                

        messagebox.showerror("Error", "Login failed. Please check your username and password.")


def main():
    root = tk.Tk()
    registered_accounts = []  

    def show_register_window():
        register_window = tk.Toplevel(root)
        RegisterWindow(register_window, registered_accounts, show_login_window)

    def show_login_window():
        login_window = tk.Toplevel(root)
        LoginWindow(login_window, registered_accounts, show_home_page)

    def show_home_page():
        home_page = tk.Toplevel(root)
        home_page.title("Home Page")

    register_button = ttk.Button(root, text="Register", command=show_register_window)
    login_button = ttk.Button(root, text="Login", command=show_login_window)

    register_button.pack(pady=20)
    login_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
