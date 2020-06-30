#REQUIRES BS4
from bs4 import BeautifulSoup

html = "<head> <title>TitleThing</title> <body> <p>Test</p> <p>P2</p> <p id='a'>HAS ID 'A'</p> </body> </head>"

#get html from local var
#soup = BeautifulSoup(html, 'html.parser')

#get html from external URL
from urllib import request
url = "https://www.google.com/"
response = request.urlopen(url)
src = response.read()
soup = BeautifulSoup(src, 'html.parser')

### soup.find ###
#Find 1st
#f = soup.find('p')
#Find all
#f = soup.find_all('p')
#Find by ID
#f = soup.find(id='id')
#Find by Class
#f = soup.find(class_='class')
#Find by Attribute
#f = soup.find(attrs={"name":"value"})

### soup.select ###
#lets you use CSS selecters
#f = soup.select('.class')
#f = soup.select('#id')

#.get_text() to get text w/o html

f = soup.find_all(class_="NKcBbd")

for i in range(len(f)):
	print(f[i].get_text())
	print(f[i]['href'])
