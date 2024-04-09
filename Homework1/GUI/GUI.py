import tkinter as tk
from Homework1.Quadratic_solver.src.quadratic_solver.quadratic_solver import solve_quadratic


def calculate():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    result = solve_quadratic(a, b, c)
    result_label.config(text=str(result))

root = tk.Tk()
root.geometry("600x300")  # Set the window size to 300 pixels wide and 200 pixels tall

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