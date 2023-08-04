# The pdb module provides a number of different methods that can be used to debug your code. 
# The most basic method is the run() method, which starts the interactive prompt and runs the code until a breakpoint is hit. 
# Here's an example of how to use the run() method:
import pdb

def add_numbers(a, b):
    result = a + b
    return result

pdb.run("add_numbers(1, 2)")

# Another useful method provided by the pdb module is the runcall() method. 
# This method runs a function and starts the interactive prompt when the function is called. 
# Here's an example of how to use the runcall() method:
import pdb

def add_numbers(a, b):
    result = a + b
    return result

pdb.runcall(add_numbers, 1, 2)

# Another method provided by the pdb module is the set_trace() method, it allows you to set a breakpoint in your code at the point where you call this method. 
# Here's an example of how to use the set_trace() method:
import pdb

def add_numbers(a, b):
    pdb.set_trace()
    result = a + b
    return result

add_numbers(1, 2)