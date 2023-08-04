# In a doubly linked list, each node has a reference to both the next and previous nodes. 
# This allows us to traverse the list in both directions, making doubly linked lists more flexible than singly linked lists.
# Now that we have a basic understanding of doubly linked lists, let's see how we can implement them in Python.
# We can start by modifying our Node class from our previous post on linked lists to include a reference to the previous node as well.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Next, we can create a DoublyLinkedList class to represent the doubly linked list itself. 
# This class will have a head and tail instance variables to keep track of the first and last nodes in the list.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

# We can then add various methods to the DoublyLinkedList class to manipulate the list. 
# For example, we can add a method to add a new node to the list, a method to remove a node from the list, and a method to find a specific node in the list.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev
                return
            current_node = current_node.next
    
    def find_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None 