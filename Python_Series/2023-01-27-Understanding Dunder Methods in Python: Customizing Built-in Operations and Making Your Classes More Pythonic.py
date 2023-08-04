# In Python, dunder methods, also known as "magic" or "special" methods, are used to define how objects of a class behave in certain situations.
# One of the most commonly used dunder methods is the __init__() method. 
# This method is used to initialize an object when it is created. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value

# Create an object of MyClass
obj = MyClass(5)

# Print the value attribute of the object
print(obj.value) # Output: 5

# Another commonly used dunder method is the __str__() method. 
# This method is used to define how an object should be represented as a string. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'MyClass object with value: {}'.format(self.value)

# Create an object of MyClass
obj = MyClass(5)

# Print the object
print(obj) # Output: 'MyClass object with value: 5'

# Another useful dunder method is the __add__() method. 
# This method is used to define how two objects of a class should be added together. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MyClass(self.value + other.value)

# Create two objects of MyClass
obj1 = MyClass(5)
obj2 = MyClass(10)

# Add the two objects
result = obj1 + obj2

# Print the value attribute of the result object
print(result.value) # Output: 15

# Another dunder method is the __eq__() method. 
# This method is used to define how two objects of a class should be compared for equality. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

# Create two objects of MyClass
obj1 = MyClass(5)
obj2 = MyClass(5)
obj3 = MyClass(10)

# Compare the two objects
print(obj1 == obj2) # Output: True
print(obj1 == obj3) # Output: False

# The __len__() method is used to define the length of an object. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(self.value)

# Create an object of MyClass
obj = MyClass([1, 2, 3, 4, 5])

# Get the length of the object
print(len(obj)) # Output: 5

# The __iter__() method is used to define an iterator for an object. 
# Here's an example of how to use it:
class MyClass:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            raise StopIteration
        result = self.value[self.index]
        self.index += 1
        return result

# Create an object of MyClass
obj = MyClass([1, 2, 3, 4, 5])

# Iterate over the object
for item in obj:
    print(item)
# Output: 1, 2, 3, 4, 5