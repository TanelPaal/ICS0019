"""
@author: eikivi
"""
my_variable = 1  # in the global scope


def my_function():
    global my_variable  # BAD PRACTICE!
    my_variable = 2  # in the function scope
    print("Inside function", my_variable)


print("Outside function", my_variable)
my_function()  # prints 2
print("Outside function", my_variable)
