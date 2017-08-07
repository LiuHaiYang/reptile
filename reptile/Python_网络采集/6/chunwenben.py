#test
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(textPage.read())

# #对文档进行UTF-8编码
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
# bsObj = BeautifulSoup(html)
# content = bsObj.find('',{''}).get_text()
# content = bytes(content,"UTF-8")
# content = content.decode("UTF-8")
# print(str(textPage.read(),'utf-8'))


