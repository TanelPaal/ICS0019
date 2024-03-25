"""
@author: eikivi
"""


class MyCounter:
    def __init__(self, x):
        self.x = x

    def add_1(self):
        self.x += 1


my_counter = MyCounter(0)
my_counter.add_1()
my_counter.add_1()
my_counter.add_1()
print(my_counter.x)
