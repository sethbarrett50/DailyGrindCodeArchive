# In Python, you can read and write files using the built-in open() function and the read(), readline(), write(), and close() methods of file objects. 
# For example:
# Open a file for writing
f = open("test.txt", "w")

# Write some text to the file
f.write("Hello, World!")

# Close the file
f.close() 

# You can also open a file for reading using the "r" mode, like this:
# Open a file for reading
f = open("test.txt", "r")

# Read the contents of the file
contents = f.read()

# Print the contents
print(contents)  # Output: Hello, World!

# Close the file
f.close() 

# You can use the readline() method to read a single line of the file at a time, or you can use a for loop to iterate over the lines of the file. 
# For example:
# Open a file for reading
f = open("test.txt", "r")

# Read and print each line of the file
for line in f:
    print(line)

# Close the file
f.close() 

# You can use the with statement to automatically close a file when you're done with it. 
# For example:
# Open a file for reading
with open("test.txt", "r") as f:
    # Read and print each line of the file
    for line in f:
        print(line)