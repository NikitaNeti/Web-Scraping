from bs4 import BeautifulSoup
import requests

result = requests.get("http://www.google.com")
content = result.text
soup = BeautifulSoup(content,"lxml")
print(soup)