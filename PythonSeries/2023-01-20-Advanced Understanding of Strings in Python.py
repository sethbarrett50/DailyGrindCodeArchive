# In Python, you can concatenate two or more strings using the + operator. 
# For example:
string1 = "Hello"
string2 = "World"
string3 = string1 + ", " + string2 + "!"
print(string3) # Output: "Hello, World!"

# You can also replicate a string by using the * operator. 
# For example:
string = "Python "
print(string * 3) 
# Output: "Python Python Python "

# String slicing is a technique used to extract a specific part of a string in Python. 
# It allows you to access individual characters or a range of characters within a string.
# For example, let's say you have the following string:
string = "Python is fun!"

# To get the first character of the string, you can use the following code:
print(string[0]) # Output: "P"

# To get the last character of the string, you can use the following code:
print(string[-1]) # Output: "!"

# To get a range of characters within the string, you can use the following code:
print(string[7:11]) # Output: "is "

# You can also use negative indexing to slice the string from the end, for example:
print(string[-5:-1]) # Output: "fun"

# You can also leave the starting or ending index blank to slice the string from the beginning or to the end respectively. 
# For example:
print(string[:5]) # Output: "Pytho"
print(string[7:]) # Output: "is fun!"

# You can also use the step parameter to skip characters while slicing. 
# The step parameter is added after the starting and ending indices and is separated by a colon. 
# For example, to get every second character in a string:
print(string[::2]) # Output: "Pto sfn"

# Python provides a number of built-in methods for working with strings. 
# Some of the most commonly used methods are:
string = "Python is fun!"
print(len(string)) # Output: 14
print(string.upper()) # Output: "PYTHON IS FUN!"
print(string.lower()) # Output: "python is fun!"
print(string.find("is")) # Output: 7
print(string.replace("is", "was")) # Output: "Python was fun!"
print(string.split(" ")) # Output: ['Python', 'is', 'fun!']
string = "   Python is fun!   "
print(string.strip()) # Output: "Python is fun!"