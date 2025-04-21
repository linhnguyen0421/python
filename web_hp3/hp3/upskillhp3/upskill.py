import tkinter as tk
from tkinter import messagebox


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
      game_window = GameWindow()
      game_window.run()
    else:
      messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng.")


class GameWindow:

  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Trò chơi X và O")

    self.current_player = "X"

    self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(3):
      for j in range(3):
        self.buttons[i][j] = tk.Button(
            self.root,
            text="",
            width=10,
            height=3,
            command=lambda row=i, col=j: self.click(row, col))
        self.buttons[i][j].grid(row=i, column=j)

  def click(self, row, col):
    if not self.buttons[row][col]["text"]:
      self.buttons[row][col]["text"] = self.current_player
      if self.check_winner(row, col):
        messagebox.showinfo("Chúc mừng",
                            f"Người chơi {self.current_player} thắng!")
        self.reset_game()
      elif self.check_draw():  
        messagebox.showinfo("Hòa", "Trò chơi hòa!")
        self.reset_game()
      else:
        self.switch_player()

  def check_winner(self, row, col):
    # Kiểm tra hàng và cột
    if all(self.buttons[row][i]["text"] == self.current_player for i in range(3)) or \
       all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
      return True
    # Kiểm tra đường chéo chính
    if row == col and all(self.buttons[i][i]["text"] == self.current_player
                          for i in range(3)):
      return True
    # Kiểm tra đường chéo phụ
    if row + col == 2 and all(
        self.buttons[i][2 - i]["text"] == self.current_player
        for i in range(3)):
      return True
    return False

  def check_draw(self):
    return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))

  def switch_player(self):
    self.current_player = "O" if self.current_player == "X" else "X"

  def reset_game(self):
    for i in range(3):
      for j in range(3):
        self.buttons[i][j]["text"] = ""
    self.current_player = "X"

  def run(self):
    self.root.mainloop()


if __name__ == "__main__":
  login_window = LoginWindow(tk.Tk())
  login_window.root.mainloop()
