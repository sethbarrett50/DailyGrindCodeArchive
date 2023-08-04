# The hashlib library in Python is a powerful tool for creating and working with cryptographic hash functions.
# Here is an example of how to use the hashlib library to create a hash of a message using the SHA-256 algorithm:
import hashlib

message = "Hello, World!"

# Create a new SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the bytes of the message
hash_object.update(message.encode())

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()

print(hash_hex)

# Another feature of the hashlib library is the ability to create a hash from a file. 
# Here's an example of how to create a hash of a file using the SHA-256 algorithm:
import hashlib

with open("example.txt", "rb") as f:
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Read the file in chunks
    while True:
        data = f.read(4096)
        if not data:
            break
        hash_object.update(data)

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

print(hash_hex)