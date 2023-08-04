# The multiprocessing module allows you to create multiple processes that run concurrently in separate memory spaces. 
# This is useful for parallelizing computationally intensive tasks that do not need to share memory. 
# Here's an example of how to use the Pool class of the multiprocessing module to parallelize a function:
from multiprocessing import Pool

def square(x):
    return x*x

# Create a pool of 4 worker processes
with Pool(4) as p:
    # Apply the square function to each element of the input list
    result = p.map(square, [1, 2, 3, 4, 5])

print(result)  # Output: [1, 4, 9, 16, 25]

# The threading module allows you to create multiple threads that run concurrently in the same memory space. 
# This is useful for parallelizing tasks that need to share memory. 
# Here's an example of how to use the Thread class of the threading module to parallelize a function:
from threading import Thread

def square(x):
    return x*x

# Create a list of input values
input_list = [1, 2, 3, 4, 5]

# Create a list to store the results
result = []

# Create a new thread for each input value
threads = [Thread(target=square, args=(x, result)) for x in input_list]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(result)  # Output: [1, 4, 9, 16, 25]