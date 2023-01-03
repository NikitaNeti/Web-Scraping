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
    tag3 = soup.title
    print(tag3)
    print(tag3.parent)
    # soup = BeautifulSoup("<b>Extremely bold</b>","lxml")
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

# Going sideways

sibling_soup = BeautifulSoup("<a><b>TutorialsPoint</b><c><strong>The Biggest Online Tutorials Library, It's all Free</strong></b></a>",'lxml')
print(sibling_soup.prettify())

#.next_sibling and .previous_sibling
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

print(sibling_soup.b.next_element)
print(sibling_soup.a.previous_element)

#.next_siblings and .previous_siblings
# for sibling in soup.a.next_siblings:
#     print(sibling)

# for s in soup.find(id="link3").previous_siblings:
#     print(s)

for element in sibling_soup.b.next_elements:
    print(repr(element))   





