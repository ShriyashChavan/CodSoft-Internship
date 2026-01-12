# Shrish
import tkinter as tk
from tkinter import messagebox
# Calculator functions
def button_click(value):
    current = display_var.get()
    if current == "0" and value != ".":
        display_var.set(str(value))
    else:
        display_var.set(current + str(value))
# display
def button_clear():
    display_var.set("0")
# operations
def button_operation(op):
    global first_num, current_op
    try:
        first_num = float(display_var.get())
    except:
        first_num = 0
    current_op = op
    display_var.set("0")
# equals
def button_equals():
    global first_num, current_op
    try:
        second_num = float(display_var.get())
        if current_op == "+":
            result = first_num + second_num
        elif current_op == "-":
            result = first_num - second_num
        elif current_op == "*":
            result = first_num * second_num
        elif current_op == "/":
            if second_num == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = first_num / second_num
        elif current_op == "%":
            if second_num == 0:
                messagebox.showerror("Error", "Cannot modulo by zero!")
                return
            result = first_num % second_num
        else:
            result = second_num
        display_var.set(str(result))
        first_num = result
    except:
        messagebox.showerror("Error", "Invalid calculation!")

# Create main window
root = tk.Tk()

# Gloobal variables
display_var = tk.StringVar()
display_var.set("0")
first_num = 0
current_op = ""
root.title("Calculator")
root.geometry("280x380")
root.resizable(False, False)

# Display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 18), 
                   justify="right", state="readonly", bd=5)
display.pack(pady=15, padx=10, ipady=15, fill="x")

# Button frane
frame = tk.Frame(root)
frame.pack(pady=10)

# operation
buttons = [
    ('C', 0, 0, 1), ('%', 1, 0, 1), ('/', 2, 0, 1), ('', 3, 0, 1),
    ('7', 0, 1, 1), ('8', 1, 1, 1), ('9', 2, 1, 1), ('*', 3, 1, 1),
    ('4', 0, 2, 1), ('5', 1, 2, 1), ('6', 2, 2, 1), ('-', 3, 2, 1),
    ('1', 0, 3, 1), ('2', 1, 3, 1), ('3', 2, 3, 1), ('+', 3, 3, 1),
    ('0', 0, 4, 1), ('.', 1, 4, 1), ('=', 2, 4, 2)
]
#creating buttons
for (text, col, row, span) in buttons:
    if text == 'C':
        btn = tk.Button(frame, text=text, font=("Arial", 16), width=7, height=2,
                        command=button_clear, bg="orange", fg="white")
    elif text in ['+', '-', '*', '/', '%']:
        btn = tk.Button(frame, text=text, font=("Arial", 16), width=7, height=2,
                        command=lambda t=text: button_operation(t), bg="#ff9500", fg="white")        
    elif text == '=':
        btn = tk.Button(frame, text=text, font=("Arial", 16), width=14, height=2,
                        command=button_equals, bg="lightgreen", fg="white")
    elif text:
        btn = tk.Button(frame, text=text, font=("Arial", 16), width=7, height=2,
                        command=lambda v=text: button_click(v), bg="lightgray")
    else:
        continue
    
    if span == 2:
        btn.grid(column=col, row=row, padx=3, pady=3, columnspan=2, sticky="nsew")
    else:
        btn.grid(column=col, row=row, padx=3, pady=3, sticky="nsew")

# grid weights
for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)
# runs the applicationsss
root.mainloop()
