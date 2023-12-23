from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pasamelo.net')
bs = BeautifulSoup(html, 'html.parser')
print(bs)
