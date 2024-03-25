"""
@author: eikivi
"""
my_variable = 3  # in the global scope


def my_function():
    my_variable = 2  # in the function scope
    print("Inside function", my_variable)


my_function()  # prints 2
print("Outside function", my_variable)  # prints 3
