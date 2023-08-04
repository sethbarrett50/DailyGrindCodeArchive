# Dictionaries are a fundamental data structure in Python and are used to store key-value pairs in a way that is efficient and easy to manage.
# An example of implementation of a dictionary in Python is as follows:
# create an empty dictionary
my_dict = {}

# create a dictionary with initial values
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# create a dictionary using dict() constructor
my_dict = dict(name='John', age=30, city='New York')

# You can access the value of a dictionary by using its key inside square brackets [], like this:
name = my_dict['name']
print(name)  # prints 'John'

# You can also use the get() method to access a value, which is safer than using square brackets because it returns None if the key is not found, instead of raising a KeyError:
age = my_dict.get('age')
print(age)  # prints 30

not_exist = my_dict.get('not_exist')
print(not_exist) # prints None

# Dictionaries also support several useful methods for adding, modifying, and deleting elements. 
# Some of the most commonly used methods are:

'''update(): adds key-value pairs from another dictionary or an iterable of key-value pairs'''

# adding key-value pairs from another dictionary
my_dict.update({'gender': 'male', 'email': 'john@example.com'})
print(my_dict) 
# prints {'name': 'John', 'age': 30, 'city': 'New York', 'gender': 'male', 'email': 'john@example.com'}

# adding key-value pairs from an iterable
my_dict.update(zip(['name', 'age'], ['Jane', 25]))
print(my_dict) 
# prints {'name': 'Jane', 'age': 25, 'city': 'New York', 'gender': 'male', 'email': 'john@example.com'}

'''pop(): removes and returns a key-value pair by its key'''
email = my_dict.pop('email')
print(email) 
# prints 'john@example.com'
print(my_dict) 
# prints {'name': 'Jane', 'age': 25, 'city': 'New York', 'gender': 'male'}

'''popitem(): removes and returns an arbitrary key-value pair as a tuple'''
gender = my_dict.popitem()
print(gender) 
# prints ('gender', 'male')
print(my_dict) 
# prints {'name': 'Jane', 'age': 25, 'city': 'New York'}

'''del : deletes the key-value pair by its key'''
del my_dict['city']
print(my_dict) 
# prints {'name': 'Jane', 'age': 25}

'''len(): returns the number of key-value pairs in the dictionary'''
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(len(my_dict)) # prints 3

'''keys() and values(): return an iterable of the keys and values respectively'''
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

'''items(): returns an iterable of key-value pairs as tuples'''
for key, value in my_dict.items():
    print(key, value)

'''in: checks if a key is present in the dictionary'''
if 'name' in my_dict:
    print('name is present')
else:
    print('name is not present')