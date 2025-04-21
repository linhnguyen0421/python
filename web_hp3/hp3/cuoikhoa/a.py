from tkinter import *
import tkinter as tk
from tkinter import messagebox

class  window:
    def __init__(self,root):
        self.root=root

        self.root.title("Game X O")
        self.root.geometry("500x500")

        self.username = tk.Label(root, text="Username")
        self.password = tk.Label(root, text="Password")
        self.username.grid(row=0, column=0)
        self.password.grid(row=1, column=0)
        self.username_entry = tk.Entry(root)
        self.password_entry = tk.Entry(root,show="*")
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)  
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "viet" and password == "noob":
            self.root.destroy()
            a = gamewindow(self.root)
            a.run()
        else:
            messagebox.showerror("dang nhap that bai!")

class gamewindow:
  def __init__(self, root):
      self.root = tk.Tk()
      self.root.title("Game X O")
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
            self.buttons[i][j].grid(row=i,column=j)
  def click(self, row, col):
        if not self.buttons[row][col]['text']:
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("chuc mung , ng choi",self.current_player+"da chien thang")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Hòa", "Trò chơi hòa")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

  def check_winner(self, row, col):
        if self.check_row(row) or self.check_col(col) or self.check_duong_cheo(row, col):
            return True

  def check_draw(self):
        return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))

  def check_row(self, row):
        if all(self.buttons[row][i]["text"] == self.current_player for i in range(3)):
            return True

  def check_col(self, col):
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True

  def check_duong_cheo(self, row, col):
        if row == col and all(self.buttons[i][j]['text'] == self.current_player for i in range(3) for j in range(3)):
            return True
        if row + col == 2 and all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True
        return False

  def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.current_player = 'X'

  def run(self):
        self.root.mainloop()

if __name__ == "__main__":
  login = window(tk.Tk())
  login.root.mainloop()
