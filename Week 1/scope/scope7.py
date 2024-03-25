"""
@author: eikivi
"""


class MyClass:
    A = 'class variable'

    def __init__(self, c):
        self.c = c  # instance variable

    def my_method(self):
        """
        methods can only be called on the instance of the class.
        So this will work:
        `MyClass(4).my_method()  # prints 4`
        But this will not work:
        `MyClass.my_method()  # raises Error`

        self refers to the instance. The instance has the attributes of the class including:

        - class variables (i.e `self.A`)
        - class methods  (i.e. `self.my_class_method()`)
        - static methods (i.e. `self.my_static_method()`)

        and self also has attributes of the instance including:

        instance variables (i.e. `self.c`)
        instanct methods (i.e. `self.my_method`)
        """
        print(self.c)

    @classmethod
    def my_class_method(cls):
        """
        cls refers to the class. It has attributes of the class, including:
        - class variables (i.e `self.A`)
        - class methods  (i.e. `self.my_class_method()`)
        - static methods (i.e. `self.my_static_method()`)
        """
        print(cls.A)

    @staticmethod
    def my_static_method():
        """
        static methods work like a regular function that is not in a class.
        They do not have access to variables and methods in the class or the instance.
        They are only in the class for organizational reasons, and may be better
        outside the class.
        """
        print('static method called')


print(MyClass.A)  # prints 'class variable'
MyClass.my_class_method()  # prints 'class variable'
MyClass.my_static_method()  # prints 'static method called'

my_instance = MyClass('my instance variable')
my_instance.my_class_method()  # prints 'class variable'
print(my_instance.c)  # prints 'my instance variable'
my_instance.my_method()  # prints 'my instance variable'
my_instance.my_static_method()  # prints 'static method called'
