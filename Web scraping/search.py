from bs4 import BeautifulSoup
with open("index.html") as fp:
    soup = BeautifulSoup(fp,'lxml')

    # a = soup.find_all('b')
    # print(a)

    # a = soup.find_all(['a','b'])
    # print(a)

    # a = soup.find_all(True)
    # print(a)

# name argument
    a = soup.find_all("title")
    print(a)

# keyword argument
    a = soup.find_all(id='link2')
    print(a)

# Searching by CSS class 
    a = soup.find_all('a',class_='sister')
    print(a)

# string argument
    a = soup.find_all(string='Elsie')
    b = soup.find_all(text='Lacie')
    print(b)

    a = soup.find_all("a", string="Elsie")
    print(a)   

#limit argument
    a = soup.find_all("a",limit=2)
    print(a)  
    
# recursive argument
    a=soup.html.find_all("title", recursive=False)
    print(a)