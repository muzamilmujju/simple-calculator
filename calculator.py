import tkinter as tk

def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


window = tk.Tk()
window.title("Simple Calculator")

entry = tk.Entry(window, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1),  ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=("Arial", 18), command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=10, pady=10)


clear_button = tk.Button(window, text="C", font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

equal_button = tk.Button(window, text="=", font=("Arial", 18), command=calculate)
equal_button.grid(row=6, column=0, columnspan=4)

window.mainloop()
