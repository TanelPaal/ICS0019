"""
@author: eikivi
"""


class A:
    my_variable = 'hi'

    @staticmethod
    def my_function():
        print('my_function called')


print(A.my_variable)
A.my_function()
