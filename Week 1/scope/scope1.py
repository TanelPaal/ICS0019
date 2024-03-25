"""
@author: eikivi
"""
my_variable = 1  # in the global scope


def my_function():
    print("Inside function", my_variable)


my_function()

print("Outside function", my_variable)
