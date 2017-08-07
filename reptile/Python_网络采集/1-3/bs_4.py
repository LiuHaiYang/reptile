
from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
	html = urlopen("http://www.cnblogs.com/pythongo/p/6413023.html")
except HTTPError as e:
	print(e) 
bsobj = BeautifulSoup(html.read())
print(bsobj.title)
print(bsobj.h1)