def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_hello():
    print("Hello World!")


say_hello()
print("-----------------------------")
blaah = decorator(say_hello)
print(blaah)
blaah()
say_hello()
