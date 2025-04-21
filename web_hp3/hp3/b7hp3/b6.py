from tkinter import *
from tkinter import messagebox

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

window = Tk()
window.title("Tkinter Menu Example")

# Tạo thanh công cụ menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Create File menu and add commands
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# Create Edit menu and add commands
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Create Help menu and add commands
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)



window.mainloop()
