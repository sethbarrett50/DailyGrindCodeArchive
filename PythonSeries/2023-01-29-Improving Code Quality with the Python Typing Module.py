# The typing module provides a number of different types that can be used to indicate the type of a variable, function, or method. 
# For example, the List type can be used to indicate that a variable is a list of a specific type of elements. 
# Here's an example of how to use the List type:
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)

print(add_numbers([1, 2, 3, 4, 5])) # Output: 15
print(add_numbers([1, 2, '3', 4, 5])) # Output: TypeError

# Another useful type provided by the typing module is the Tuple type. 
# This type can be used to indicate that a variable is a tuple of specific types. 
# Here's an example of how to use the Tuple type:
from typing import Tuple

def add_numbers(numbers: Tuple[int, int]) -> int:
    return sum(numbers)

print(add_numbers((1, 2))) # Output: 3
print(add_numbers((1, '2'))) # Output: TypeError

# Another type provided by the typing module is the Union type. 
# It allows you to indicate that a variable can be of one of multiple types. 
# Here's an example of how to use the Union type:
from typing import Union

def add(a: Union[int,float], b: Union[int,float])-> Union[int,float]:
    return a+b

print(add(1, 2)) # Output: 3
print(add(1.1, 2)) # Output: 3.1