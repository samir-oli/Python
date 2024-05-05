#write a decorator that measures the time a function takes to execute

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)

#create a decorator to print the function name and the values of
#  its arguements every time the function is called

