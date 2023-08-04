# Inheritance is a way to create a new class that is a modified version of an existing class. 
# The new class is called the subclass, and the existing class is the superclass. 
# The subclass inherits attributes and behavior from the superclass, and can also have additional attributes and behavior of its own.
# For example:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # call superclass's __init__ method
        self.breed = breed
        self.toy = toy
    
    def play(self):
        print(f"{self.name} plays with {self.toy}")

cat1 = Cat("Kitty", "Siamese", "String")
print(cat1.name)  # prints "Kitty"
print(cat1.species)  # prints "Cat"
cat1.make_sound()  # prints "Some generic animal sound"
cat1.play()  # prints "Kitty plays with String" 

# Polymorphism is the ability of a subclass to override or extend the behavior of its superclass. 
# For example:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy
    
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof")

animals = [Cat("Kitty", "Siamese", "String"), Dog("Fido", "Labrador")]
for animal in animals:
    animal.make_sound() 
