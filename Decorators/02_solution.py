#create a decorator to print the function name and the values of
#  its arguements every time the function is called
def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper



def hello():
    print("hello")

def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")

greet("chai", greeting="hanji")