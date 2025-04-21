from tkinter import ttk
import tkinter as tk

class window:
  def __init__(self,a):
      self.a = a
      self.a.title("may tinh cam tay")
      self.display_var = tk.StringVar()
      entry = ttk.Entry(a,textvariable=self.display_var )
      entry.grid(row=0,column=0,columnspan=4,sticky="nsew")
      buttons = [
        "1", "2", "3", "+",
        "4", "5", "6", "-",
        "7", "8", "9", "*",
        "0", ".", ":", "=",
        "C"
      ]
      row_val = 1
      col_val = 0
      for button in buttons:
        ttk.Button(a, text=button, command=lambda b=button: self.on_button_click(b)).grid (row=row_val,column=col_val)
        col_val+=1
        if col_val>3:
            col_val=0
            row_val+=1
  def clear_entry(self):
      self.display_var.set("")
   
  def on_button_click(self, button):
    current_text = self.display_var.get()
    if button == "C":
      self.clear_entry(button)
    elif button == "=":
        try:
          result = str(eval(current_text))
          self.display_var.set(result)
        except Exception as e:
          self.display_var.set("loi")
    else:
      new_text=current_text + button
      self.display_var.set(new_text)

if __name__ == "__main__":
  cs = tk.Tk()
  app = window(cs)
  cs.mainloop()