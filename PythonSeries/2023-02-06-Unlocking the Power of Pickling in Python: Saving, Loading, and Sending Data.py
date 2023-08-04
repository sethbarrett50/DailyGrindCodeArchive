# The pickle library for Python is a powerful tool for serializing and deserializing Python objects
# Here's an example of how to use pickle to save a list of integers to a file:
import pickle

numbers = [1, 2, 3, 4, 5]

with open("numbers.pickle", "wb") as file:
    pickle.dump(numbers, file)

# To load the data back from the file, you can use the pickle.load() function. Here's an example:
with open("numbers.pickle", "rb") as file:
    numbers = pickle.load(file)

print(numbers) 
# [1, 2, 3, 4, 5]

# Pickling can also be used to send data over the network, for example using sockets. 
# Here's an example of using pickling to send an object over a socket:
import socket
import pickle

def send_obj(sock, obj):
    data = pickle.dumps(obj)
    sock.sendall(data)

def recv_obj(sock):
    data = b''
    while True:
        part = sock.recv(1024)
        data += part
        if len(part) < 1024:
            break
    return pickle.loads(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1234))

obj = {'a':1,'b':2,'c':3}
send_obj(sock, obj)
received_obj = recv_obj(sock)
print(received_obj)