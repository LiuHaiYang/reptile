#-*-coding:utf-8 -*-
import urllib
from urllib.request import Request,urlopen
from urllib.error import URLError
from bs4 import  BeautifulSoup
import re

#糗事百科爬虫类


page = 10
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
def getHTML(url):  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  
    req = Request(url, headers=headers)  
    return urlopen(req) 

try:
    rep = getHTML(url)
    # print(rep.read().decode('utf-8'))
    content = BeautifulSoup(rep)
    content_all= content.find_all("",{"class":"article block untagged mb15"})
    for item in content_all:
        name = item.h2.get_text()
        p = item.span.get_text()
        pinglun = item.find('i',{'class':'number'}).get_text()
        print('用户名：' + name)
        print('内容：' + p)
        print('评论数：' + pinglun)
        print('=========================================')
except URLError as e:
    if hasattr(e,"code"):
        print(e.code())
    if hasattr(e,"reason"):
        print(e.reason())
