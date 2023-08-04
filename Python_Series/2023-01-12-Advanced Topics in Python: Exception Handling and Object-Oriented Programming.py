# Exception handling is an important tool to have in your programming toolkit, as it helps you to write more robust and reliable code. 
# For example:
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# In Python, we can create classes to define our own objects. 
# For example:
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Labrador")
print(dog1.name)  
# prints "Fido"
dog1.bark()  
# prints "Woof!" 