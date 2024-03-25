"""
@author: eikivi
"""

MY_CONSTANT = 'constant outside of the class'


class MyClass:
    print(MY_CONSTANT)
    print('lines in my_class are executed')

    @staticmethod
    def my_function():
        print('my_function called')

    my_function()
