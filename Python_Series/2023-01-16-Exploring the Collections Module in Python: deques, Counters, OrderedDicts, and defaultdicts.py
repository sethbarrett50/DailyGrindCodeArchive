# Here are some examples of how to use data types:
from collections import deque, Counter, OrderedDict, defaultdict

# deque example
q = deque(["a", "b", "c"])
q.appendleft("d")  # add an element to the left side
print(q)  # deque(['d', 'a', 'b', 'c'])
q.pop()  # remove and return an element from the right side
print(q)  # deque(['d', 'a', 'b'])

# Counter example
c = Counter(["a", "b", "c", "a", "b", "b"])
print(c)  # Counter({'b': 3, 'a': 2, 'c': 1})

# OrderedDict example
d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(d)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# defaultdict example
dd = defaultdict(int)  # default value is 0
dd["a"] = 1
dd["b"] = 2
print(dd["c"])  # 0

# The deque (short for double-ended queue) is a data structure that is similar to a list, but it allows efficient insertion and deletion at both ends of the sequence.
# An example of using a deque is as follows:
from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Add elements to the deque
d.appendleft(0)  # add element to the left side
d.append(4)  # add element to the right side

# Remove elements from the deque
d.popleft()  # remove and return element from the left side
d.pop()  # remove and return element from the right side

# Iterate over the elements of the deque
for x in d:
    print(x) 

# The Counter is a dictionary subclass from the collections module that is used for counting occurrences of hashable objects.
# An example of using a Counter is as follows:
from collections import Counter

# Count the frequency of elements in a list
c = Counter(["a", "b", "c", "a", "b", "b"])
print(c)  # Counter({'b': 3, 'a': 2, 'c': 1})

# Convert the Counter to a dictionary
d = dict(c)
print(d)  # {'a': 2, 'b': 3, 'c': 1}

# Use the most_common method to get the most frequent elements
print(c.most_common(2))  # [('b', 3), ('a', 2)]

# Use arithmetic operations to add or subtract counts
c2 = Counter({"a": 1, "b": 2, "c": 3})
c3 = c + c2  # add counts
c4 = c - c2  # subtract counts
print(c3)  # Counter({'b': 5, 'a': 3, 'c': 4})
print(c4)  # Counter({'b': 1, 'a': 1, 'c': -2})

# The OrderedDict is a dictionary subclass from the collections module that remembers the order that keys were added to the dictionary.
# An example of using an OrderedDict is as follows:
from collections import OrderedDict

# Create an OrderedDict
d = OrderedDict()

# Add elements to the OrderedDict
d["a"] = 1
d["b"] = 2
d["c"] = 3

# Iterate over the elements of the OrderedDict
for k, v in d.items():
    print(k, v)

# Output the elements in the order they were added
print(d)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# The defaultdict is a dictionary subclass from the collections module that provides a default value for missing keys.
# An example of using a defaultdict is as follows:
from collections import defaultdict

# Create a defaultdict with a default value of 0
dd = defaultdict(int)

# Add elements to the defaultdict
dd["a"] = 1
dd["b"] = 2

# Access a missing key
print(dd["c"])  # 0

# Use a default factory function to provide a default value
def default_factory():
    return "default value"

dd2 = defaultdict(default_factory)

# Access a missing key
print(dd2["c"])  # "default value" 