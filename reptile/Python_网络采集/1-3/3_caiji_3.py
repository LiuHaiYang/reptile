from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageurl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageurl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^/wiki/")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇见了新的页面
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")