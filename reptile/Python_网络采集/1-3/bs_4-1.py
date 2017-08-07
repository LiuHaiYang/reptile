from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
	html = urlopen("http://www.cnblogs.com/pythongo/p/6413023.html")
except HTTPError as e:
	print(e) 
bsobj = BeautifulSoup(html.read())
try:
	title = bsobj.title
	#title = bsobj.nonExistingTag.anotherTag #nonExistingTag  虚拟的标签，anotherTag  是对他的检查和处理
except AttributeError as e:
	print('Tag was not found')
else:
	if title == None:
		print('Tag was not found')
	else:
		print(title)
# print(bsobj.title)
# print(bsobj.h1)