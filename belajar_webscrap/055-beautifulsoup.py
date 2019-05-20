# install pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

# ambil file dr html text dalam dir
'''
web = '<p>Website Dota Ampas</p>'

x = BeautifulSoup(web, 'html.parser') # default html.parser

print(x)
print(x.p.text)
'''
# ambil file dr html file dalam directory
'''
web = open('055-contoh.html', 'r') # import requests jika ingin liat dr web
x = BeautifulSoup(web, 'html.parser')
'''
# ambil fiel dr html file dari web
url = 'https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')
# print(y.prettify())

# for i in y.find_all('span', class_='mw-headline'):
#     if str(i.i) != 'None':
#         print(i.i.text)


# print(x)
# ambil title
'''
print(x.title)
print(x.title.name)
print(x.title.text)
print(x.title.string)
'''
# ambil paragraph
'''
print(x.p.text)
'''
# ambil semua paragraph
'''
# print(x.find_all('p')) # keluarnya list
for i in x.find_all('p'):
    print(i)
'''
# ambil semua list
'''
for i in x.find_all('li'):
    print(i.text)
'''
# ambil spesifik id
'''
for i in x.find(id='p1'):
    print(i)
'''
# ambil spesifik class html
'''
for i in x.find(class_='p2'): # class sudah ada di python 
    print(i)
'''
# ambil spesifik class spesifik tag
'''
for i in x.find_all('p', class_='p2'):
    print(i)
'''
# ambil <ol>
'''
data=x.ol
print(data)
for i in data.find_all('li'):
    print(i.text)
'''