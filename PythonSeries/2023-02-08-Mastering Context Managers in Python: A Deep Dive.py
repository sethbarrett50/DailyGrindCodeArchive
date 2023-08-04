# Context managers are a powerful feature in Python that allow you to manage resources, such as files or database connections, in a safe and efficient manner.
# Here's an example of how you can use a context manager to read a file:
with open('example.txt', 'r') as file:
    print(file.read())

# Another common use of context managers is to work with database connections. 
# Here's an example of how you can use a context manager to connect to a database and execute a query:
import sqlite3

with sqlite3.connect('example.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')
    results = cursor.fetchall()
    print(results)

# Here's an example of how you can create a context manager that times a block of code:
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    print('Elapsed time:', end_time - start_time)

with timer():
    # some code to be timed
    time.sleep(1)