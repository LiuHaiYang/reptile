from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError  as e:
        return None
    return title
title= getTitle("http://www.cnblogs.com/pythongo/p/6413023.html")
if title == None:
    print('Title was not found')
else:
    print(title)
