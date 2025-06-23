import requests
import re

url = 'https://example.com'

response = requests.get(url)

title = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)

if title:
    with open('title.txt', 'w') as file:
        file.write(title.group(1))
    print("Webpage title saved to title.txt.")
else:
    print("Title not found.")