# The sys module in Python provides access to various system-specific parameters and functions. 
# The first method that we'll look at is the argv attribute. 
# This attribute is a list that contains the command-line arguments passed to a Python script. 
# Here's an example of how to use it:
import sys

# Print the command-line arguments
print(sys.argv)

# Another useful method of the sys module is the exit() function. 
# This function is used to exit the interpreter by raising a SystemExit exception. 
# The optional argument passed to the function is used as the return code for the script. 
# Here's an example of how to use it:
import sys

# Exit the script with a return code of 1
sys.exit(1)

# The version attribute returns a string that contains the version of the Python interpreter. 
# Here's an example of how to use it:
import sys

# Print the Python version
print(sys.version)

# The path attribute contains a list of strings that specifies the search path for modules. 
# It can be manipulated to include new paths for importing modules. 
# Here's an example of how to use it:
import sys

# Print the module search path
print(sys.path)

# Add a new path to the search path
sys.path.append('/path/to/my/modules')

# Print the updated search path
print(sys.path)