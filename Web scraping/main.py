from bs4 import BeautifulSoup
import requests

# Fetch the pages
# result = requests.get("http://www.google.com")

#Get the page content
# content = result.text

#create the soup
# soup = BeautifulSoup(content,"lxml")
# print(soup.title)

from bs4 import BeautifulSoup
with open("index.html") as fp:
    soup = BeautifulSoup(fp,'lxml')
    soup = BeautifulSoup("<b>Extremely bold</b>","lxml")
    print(type(soup))
    print(soup.name)

    tag = soup.b
    print(type(tag))
    print(tag.name)

    tag.name = 'blockquote'
    print(tag)

    soup1 = BeautifulSoup("<p class='title'><b>The Dormouse's story</b></p>",'lxml')
    tag2 = soup1.p
    # print(tag2['class'])
    print(soup1.string)
    # print(type(soup1.string))
    soup1.string.replace_with("hiiiiiiii")
    print(tag2)


