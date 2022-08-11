def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("Decorated!")
        # function(*args, **kwargs)
        return function(*args, **kwargs)

    return wrapper

@mydecorator
def hello(name):
    # print(f"Hello, {name}!")
    return f"Hello, {name}!"

# mydecorator(hello)()

print(hello('Wah'))