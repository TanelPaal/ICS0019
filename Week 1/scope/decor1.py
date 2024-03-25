def blaahblaah(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@blaahblaah # This is a decorator. It is a function that takes a function as an argument and returns a function.
def say_hello():
    print("Hello World!")


say_hello()
