import requests
from bs4 import BeautifulSoup
URL="http://google.com"
r=requests.get(URL)
soup=BeautifulSoup(r.content,("html.parser"))
print(soup)
