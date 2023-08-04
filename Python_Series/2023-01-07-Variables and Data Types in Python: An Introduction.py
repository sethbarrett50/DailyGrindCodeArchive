# A variable is a named container for storing data. 
# In Python, you can create a variable by simply assigning a value to it using the assignment operator =. 
# This operator is used to give a value to a variable, and it consists of the equal sign (=) with the value on the right side and the variable name on the left side. 
# For example:
x = 5
y = "hello"

# An integer is a whole number, either positive or negative. For example:
x = 5
y = -10 

# A floating-point number is a number with a decimal point. For example:
x = 3.14
y = -2.718 

# A string is a sequence of characters, either letters, numbers, or symbols, enclosed in either single or double quotation marks. 
# For example:
x = "hello"
y = '12345' 

# A Boolean is a data type that can have only two values: True or False. 
# For example:
x = True
y = False 

# You can also use the type() function to check the data type of a variable. 
# For example:
x = 5
print(type(x))  
# Output: <class 'int'>

y = "hello"
print(type(y)) 
# Output: <class 'str'> 

# It's important to use the appropriate data type for your variables, as this can affect how your program behaves. 
# For example, if you try to perform arithmetic operations on a string, you'll get an error.
x = "hello"
y = 5
print(x + y)  
# Output: TypeError: can only concatenate str (not "int") to str 

# To avoid this, you can use type conversion functions to convert variables to the desired data type. 
# For example:
x = "5"
y = int(x)  
# y is now the integer 5

x = 5
y = str(x)  
# y is now the string "5" 