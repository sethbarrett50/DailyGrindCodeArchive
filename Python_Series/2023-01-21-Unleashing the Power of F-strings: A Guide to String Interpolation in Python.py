# The syntax for an f-string is very simple: you start with the letter "f" or "F" followed by a string literal, and inside that string, you can include expressions inside curly braces {}. 
# For example:
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 30 years old.

# You can also include more complex expressions inside the curly braces, like mathematical operations, function calls, or even nested f-strings:
a = 5
b = 10
c = 15
print(f"{a} * {b} = {a * b}")
# Output = 5 * 10 = 50
print(f"{a} + {b} + {c} = {a + b + c}")
# Output = 5 + 10 + 15 = 30
print(f"{a} * {b + c} = {a * (b + c)}")
# Output = 5 * 25 = 125

# F-strings also allow you to use alignment, padding, and precision options, which can be useful for formatting numbers or creating tables of data.
# To align a value to the left, right or center of the field, you can use the <, >, or ^ characters respectively, like this:
x = 1234
print(f"{x:<10}")  # align to the left with a width of 10
Output: "1234      "
print(f"{x:>10}")  # align to the right with a width of 10
Output: "      1234"
print(f"{x:^10}")     # center align with a width of 10
Output: "   1234   "

# To add padding to a value, you can use the 0 character, like this:
x = 12
print(f"{x:04}")  # pad with zeros to a width of 4
Output: "0012"

# To specify the precision of a value, you can use the . character, like this:
x = 3.14159
print(f"{x:.2f}")  # round to 2 decimal places
Output: "3.14"

