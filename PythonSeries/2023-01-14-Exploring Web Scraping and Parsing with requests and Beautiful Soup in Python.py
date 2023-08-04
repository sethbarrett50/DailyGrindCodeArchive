# requests is a library for making HTTP requests in Python. 
# It allows you to send HTTP requests (such as GET, POST, PUT, DELETE) to a web server and receive a response. 
# For example:
import requests

response = requests.get("http://www.example.com")
print(response.status_code)  
# prints 200 if the request is successful

print(response.text)  
# prints the HTML content of the webpage 

# Beautiful Soup is a library for parsing HTML and XML documents. 
# It allows you to extract data from a webpage in a more convenient and efficient way than manually parsing the HTML. 
# For example:
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>My webpage</title>
    </head>
    <body>
    <h1>Hello, world!</h1>
    <p>This is my webpage</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
title = soup.find("title").string
print(title)  
# prints "My webpage" 

# You can use requests and Beautiful Soup together to scrape data from a webpage. 
# For example:
import requests
from bs4 import BeautifulSoup

url = "http://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data from the webpage using Beautiful Soup
title = soup.find("title").string
paragraphs = soup.find_all("p")

# Print the extracted data
print(title)
for p in paragraphs:
    print(p.string) 