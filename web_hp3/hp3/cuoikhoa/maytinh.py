import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.current_value = ""
        self.result_var = tk.StringVar()
        self.last_result = None

    def press_key(self, key):
        if key == "=":
            try:
                result = str(eval(self.current_value))
                self.current_value = result
                self.last_result = result
            except Exception as e:
                self.current_value = "Lỗi"
        elif key == "C":
            self.current_value = ""
        elif key == "sqrt":
            try:
                result = str(math.sqrt(float(self.current_value)))
                self.current_value = result
                self.last_result = result
            except Exception as e:
                self.current_value = "Lỗi"
        elif key == "fact":
            try:
                result = str(math.factorial(int(self.current_value)))
                self.current_value = result
                self.last_result = result
            except Exception as e:
                self.current_value = "Lỗi"
        else:
            self.current_value += key

        self.result_var.set(self.current_value)

class CalculatorApp:
    def __init__(self, master, calculator):
        self.master = master
        self.master.title("Máy Tính Cầm Tay")

        self.calculator = calculator

        # Entry để hiển thị các số và kết quả
        entry = ttk.Entry(master, textvariable=self.calculator.result_var, font=('Arial', 14), justify='right')
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

    def on_button_click(self, button):
        self.calculator.press_key(button)

def main():
    root = tk.Tk()

    calculator = Calculator()
    app = CalculatorApp(root, calculator)

    root.mainloop()

if __name__ == "__main__":
    main()
