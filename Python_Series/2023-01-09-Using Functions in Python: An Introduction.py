# Functions are a way to group together a set of related instructions and give them a name, which can then be called upon when needed.
# For example, you might define a function like this:
def greet():
    print("Hello, World!") 

# You can call a function by simply typing its name followed by a set of parentheses. 
# For example:
greet()  
# Output: Hello, World! 

# You can also pass arguments to a function, which are values that the function can use to perform its task. 
# For example:
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  
# Output: Hello, Alice!
greet("Bob")  
# Output: Hello, Bob! 

# You can also define default values for function arguments, which will be used if no value is provided when the function is called. 
# For example:
def greet(name="World"):
    print("Hello, " + name + "!")

greet()  
# Output: Hello, World!
greet("Alice") 
# Output: Hello, Alice!
greet("Bob")  
# Output: Hello, Bob! 

# Functions can also return values using the return keyword. 
# For example:
def add(x, y):
    return x + y

result = add(5, 6)  
# result is now 11 
