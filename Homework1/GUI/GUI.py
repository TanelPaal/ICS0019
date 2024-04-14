import tkinter as tk
from quadratic_solver_tanpaa.quadratic_solver import solve_quadratic



def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    result = solve_quadratic(a, b, c)
    if isinstance(result, tuple):
        result_label.config(text=f"x1: {result[0]}, x2: {result[1]}")
    else:
        result_label.config(text=str(result))

root = tk.Tk()
root.geometry("600x300")  # Set the window size to 300 pixels wide and 200 pixels tall
root.title("Quadratic Solver")

a_label = tk.Label(root, text="Enter a:", font=("Arial", 18))
a_label.pack()
a_entry = tk.Entry(root, font=("Arial", 18))
a_entry.pack()

b_label = tk.Label(root, text="Enter b:", font=("Arial", 18))
b_label.pack()
b_entry = tk.Entry(root, font=("Arial", 18))
b_entry.pack()

c_label = tk.Label(root, text="Enter c:", font=("Arial", 18))
c_label.pack()
c_entry = tk.Entry(root, font=("Arial", 18))
c_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 18))
calculate_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack()

root.mainloop()