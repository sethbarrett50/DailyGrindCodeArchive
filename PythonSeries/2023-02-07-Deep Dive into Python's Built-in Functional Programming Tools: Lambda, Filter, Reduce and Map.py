# The lambda operator is a way to create small, anonymous functions in Python. 
# These functions can be used to perform simple operations, such as mathematical calculations or string manipulation. 
# Here's an example of a lambda function that takes a single argument and returns its square:
square = lambda x: x * x
print(square(5))   # 25

# The filter function is used to filter a list of items based on a given condition. 
# For example, we can use the filter function to find all the even numbers in a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))      # [2, 4, 6, 8, 10]

# The reduce function is used to combine all the elements of a list into a single value. 
# For example, we can use the reduce function to find the product of all the numbers in a list:
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# The map function is used to apply a function to all the elements of a list. 
# For example, we can use the map function to square all the numbers in a list:
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
print(list(squared))    # [1, 4, 9, 16, 25]