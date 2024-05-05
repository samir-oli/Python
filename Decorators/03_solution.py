# implement a decorator that caches the return values of a function, so that when its called with the same arguments , the cahced valu is returned of re-ececuting the function
import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(1)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
