"""
@author: eikivi
"""
x = 0


def add_1():
    global x
    x += 1


add_1()
add_1()
add_1()

print(x)  # prints 3
