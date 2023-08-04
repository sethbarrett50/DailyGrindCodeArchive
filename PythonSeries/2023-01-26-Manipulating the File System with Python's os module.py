# The os module in Python provides a way for your Python program to interact with the underlying operating system.
# One of the most commonly used methods of the os module is the mkdir() method. 
# This method is used to create a new directory. 
# Here's an example of how to use it:
import os

# Create a new directory
os.mkdir('new_directory')

# Another useful method of the os module is the rename() method. 
# This method is used to rename a file or directory. 
# Here's an example of how to use it:
import os

# Rename a file
os.rename('old_file.txt', 'new_file.txt')

# The remove() method is used to delete a file. 
# Here's an example of how to use it:
import os

# Delete a file
os.remove('file_to_delete.txt')

# The chdir() method is used to change the current working directory. 
# Here's an example of how to use it:
import os

# change the current working directory
os.chdir('/path/to/directory')

# The getcwd() method is used to get the current working directory. 
# Here's an example of how to use it:
import os

# get the current working directory
current_directory = os.getcwd()
print(current_directory)