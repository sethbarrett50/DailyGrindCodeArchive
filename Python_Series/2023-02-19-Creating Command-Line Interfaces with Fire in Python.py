# Python developers have a lot of options when it comes to working with command-line interfaces (CLIs) and command-line arguments. 
# One popular choice is the Fire library, which provides a simple and easy-to-use API for building CLIs. 
# Now, let's take a look at an example of how to use Fire to create a simple CLI. 
# In this example, we'll create a command-line tool that takes a string and prints it out in uppercase:
import fire

def uppercase(string: str):
    """Prints the given string in uppercase."""
    print(string.upper())

if __name__ == "__main__":
    fire.Fire(uppercase)
# When we run this script, we can pass a string to the uppercase command:
'''python script.py "Hello, World!" > In Terminal'''

# Fire also supports defining multiple commands in a single script, using the Fire() function to run multiple commands. 
# For example, we can add a new command to our script that reverses a string:
import fire

def uppercase(string: str):
    """Prints the given string in uppercase."""
    print(string.upper())
    
def reverse(string: str):
    """Prints the given string in reverse order."""
    print(string[::-1])

if __name__ == "__main__":
    fire.Fire()
# Now we can use either uppercase or reverse command:
'''python script.py uppercase "Hello, World!" > In terminal'''
'''python script.py reverse "Hello, World!"'''

# Fire also supports automatic type coercion and validation of command-line arguments. 
# This means that we can specify the expected types of our command-line arguments, and Fire will automatically convert them to the appropriate Python types. 
# For example, we can specify that the string argument should be a string:
def uppercase(string: str):
    pass
"""Prints the given string in uppercase."""


# One of the key features of Fire is its ability to automatically generate command line interfaces from Python functions and classes. 
# This allows you to quickly and easily build command line tools without having to write any additional code. 
# For example, consider the following simple Python function:
def say_hello(name: str) -> str:
    return "Hello, " + name

# With Fire, we can easily turn this function into a command line tool by simply adding the fire.Fire() decorator:
import fire

@fire.Fire
def say_hello(name: str) -> str:
    return "Hello, " + name

# Now, when we run this script from the command line, Fire will automatically generate a command line interface for the say_hello function, allowing us to call it like this:
# python script.py say_hello --name "John Doe" > In terminal


# Fire also provides a variety of other features, such as automatic type checking, support for subcommands, and the ability to define default values for arguments.
# To illustrate some of these features, let's take a look at a more advanced example. 
# This time, we'll define a class that represents a simple calculator, with methods for performing addition, subtraction, multiplication, and division:
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        return a / b

# To expose these methods as command line tools, we simply need to add the fire.Fire() decorator to the class:
import fire

@fire.Fire
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        return a / b
    
# Now, when we run this script from the command line, Fire will generate a command line interface that allows us to call each of the calculator's methods as subcommands, like this:
# python script.py add --a 2 --b 3      > In terminal
# python script.py subtract --a 2 --b 3 > In terminal
# python script.py multiply --a 2 --b 3 > In terminal
# python script.py divide --a 6 --b 3   > In terminal