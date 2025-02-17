import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to calculate the result
def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the display
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=4, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 16), bg="lightblue", fg="black", command=calculate_result)
        button.grid(row=row, column=col, columnspan=4, sticky="nsew")
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 16), bg="lightcoral", fg="black", command=clear_display)
        button.grid(row=row, column=col, sticky="nsew")
    else:
        button = tk.Button(root, text=text, font=("Arial", 16), bg="lightgray", fg="black", command=lambda t=text: update_display(t))
        button.grid(row=row, column=col, sticky="nsew")

# Configure row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
