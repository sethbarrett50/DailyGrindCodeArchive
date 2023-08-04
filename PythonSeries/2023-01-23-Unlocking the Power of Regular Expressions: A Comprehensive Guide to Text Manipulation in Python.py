# The basic syntax of a regular expression in Python is to define a pattern using a string, and then use that pattern to search for matches in another string. The search() function of the re module returns a match object if the pattern is found in the string, otherwise it returns None. 
# For example:
import re

text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
match = re.search(pattern, text)

if match:
    print("Found", match.group())
else:
    print("Not found")

# You can also use the findall() function to get a list of all the matches of a pattern in a string, and the finditer() function to get an iterator of match objects. 
# For example:
text = "The quick brown fox jumps over the lazy dog"
pattern = "o"
matches = re.findall(pattern, text)
print(matches) 
# prints ['o', 'o', 'o']

text = "The quick brown fox jumps over the lazy dog"
pattern = "o"
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())  
# prints 'o' 'o' 'o'

# One of the most powerful features of regular expressions is the ability to use special characters and quantifiers to define a pattern.
# For example:
text = "The quick brown fox jumps over the lazy dog"
pattern = "^T.+g$"
match = re.search(pattern, text)

if match:
    print("Found", match.group())
else:
    print("Not found")

# Another important feature of regular expressions is the ability to use special flags to modify the behavior of the pattern.
# For example:
text = "The quick brown fox\n jumps over the lazy dog"
pattern = "^T.+g$"
match = re.search(pattern, text, re.MULTILINE)

if match:
    print("Found", match.group())
else:
    print("Not found")

# The re.sub() method is a function of the re module in Python, which is used to perform string substitution using regular expressions. 
# It searches for all occurrences of a pattern in a string and replaces them with a replacement string.
# The basic syntax of the re.sub() method is as follows:
'''re.sub(pattern, repl, string, count=0, flags=0)'''

# You can use the re.sub() method to do this:
import re

text = "My phone number is 555-555-5555 and my friend's number is 666-666-6666"
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', 'xxx-xxx-xxxx', text)
print(new_text)