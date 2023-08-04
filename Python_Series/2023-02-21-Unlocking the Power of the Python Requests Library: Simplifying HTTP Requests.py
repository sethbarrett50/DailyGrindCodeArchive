# One of the most popular Python libraries that Python developers use is the requests library.
# The requests library is incredibly simple to use, and you can get started with it in just a few lines of code. For example, here's how you can make a simple GET request to a website:
import requests

response = requests.get("https://www.example.com")
print(response.status_code)     # 200

# You can also make other types of requests, such as POST, PUT, and DELETE. 
# Here's an example of how you can make a POST request:
import requests

data = {"name": "John Smith", "email": "john.smith@example.com"}
response = requests.post("https://www.example.com/submit", data=data)
print(response.status_code)     # 200

# One of the most powerful features of the requests library is its ability to handle various types of responses. 
# You can get the response body in various formats like json, text or binary. 
# You can also handle cookies and headers. 
# Here's an example of how you can get the response body as json:
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if response.status_code == 200:
    json_data = response.json()
    print(json_data)

