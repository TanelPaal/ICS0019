"""
@author: eikivi
"""


def my_function():
    my_variable = 2  # in the function scope
    print("Inside function", my_variable)


my_function()  # prints 2
print("Inside function", my_variable)  # raises NameError
