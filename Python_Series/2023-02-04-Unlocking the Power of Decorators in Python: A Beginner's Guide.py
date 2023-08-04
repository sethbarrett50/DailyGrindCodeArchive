# Decorators are a powerful feature in Python that allow you to modify the behavior of a function or class without changing its source code.
# Here's a simple example of a decorator that logs the arguments and return value of a function:
def log_args_and_return(func):
    def decorated(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_args_and_return
def add(a, b):
    return a + b

add(1, 2)
# Output:
# Calling add with args (1, 2) and kwargs {}
# add returned 3


# You can also apply multiple decorators to a single function by stacking them on top of each other, like so:
def multiply(a, b):
    return a * b

@log_args_and_return
@another_decorator
def multiply(a, b):
    return a * b

# Decorators can also be applied to class methods. 
# In this case, the decorator function takes the class method as an argument and returns a new method that modifies the behavior of the original method. 
# Here's an example of a decorator that logs the execution time of a method:
import time

def log_execution_time(method):
    def decorated(self, *args, **kwargs):
        start_time = time.time()
        result = method(self, *args, **kwargs)
        end_time = time.time()
        print(f"{method.__name__} took {end_time - start_time} seconds to execute")
        return result
    return decorated

class MyClass:
    def __init__(self):
        pass

    @log_execution_time
    def my_method(self):
        time.sleep(1)

my_obj = MyClass()
my_obj.my_method()
    # Output:
    # my_method took 1.000377893447876 seconds to execute