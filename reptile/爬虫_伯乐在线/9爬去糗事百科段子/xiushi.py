#-*-coding:utf-8 -*-
import urllib
from urllib.request import Request,urlopen
from urllib.error import URLError
import re

page=2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
#url = 'http://www.baidu.com'  
def getHTML(url):  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}  
    req = Request(url, headers=headers)  
    return urlopen(req) 

try:
    rep = getHTML(url)
    # print(rep.read().decode('utf-8'))
    content = rep.read().decode('utf-8')
    #
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                         '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)

    for item in items:
        print(item)
        print('====================================')
        # haveImg = re.search("img",item[3])
        # print(item.h2.get_text())
        # if not haveImg:
            # print(item[0].attrs,item[1].attrs,item[2].attrs,item[4].attrs)

except URLError as e:
    if hasattr(e,"code"):
        print(e.code())
    if hasattr(e,"reason"):
        print(e.reason())