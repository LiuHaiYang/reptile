from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsobj = BeautifulSoup(html)

images  = bsobj.findAll('img',{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
lambda_test = bsobj.findAll(lambda tag:len(tag.attrs) == 2)
for i in lambda_test:
    print(i.get_text())