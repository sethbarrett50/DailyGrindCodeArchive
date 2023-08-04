# Iterators and iterables are fundamental concepts in Python that allow you to work with collections of data in a clean and efficient manner.
# Here's an example of how you can use a for loop to iterate over a list:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# An iterator is an object that is used to iterate over an iterable object. It defines two methods, iter() and next(). 
# The iter() method returns the iterator object itself. 
# The next() method returns the next value from the iterable object. 
# If there are no more items to return, it should raise StopIteration. 
# Here's an example of how you can use the iterator protocol to manually iterate over a list:
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5

# Another example of Iterator is the built-in enumerate() function, it takes an iterable and returns an iterator that produces tuples containing the index and the corresponding item.
words = ["hello", "world"]
for index, word in enumerate(words):
    print(index, word)

# Here's an example of how you can create a custom iterator that generates the Fibonacci sequence:
class Fibonacci:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max_value:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fibonacci = Fibonacci(20)
for n in fibonacci:
    print(n)