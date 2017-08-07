#http://219.148.85.172:9380/gradeLnAllAction.do?type=ln&per=fa
# -*- coding:utf-8 -*-
import re
from urllib.request import urlopen,HTTPCookieProcessor,Request,build_opener
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
#河北工程大学绩点运算
class SDU:
 
    def __init__(self):
        self.loginUrl = 'http://219.148.85.172:9380/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=4701'
                        #http://219.148.85.172:9380/gradeLnAllAction.do?type=ln&oper=fa
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.parse.urlencode({
            'zjh':'140212130',
            'mm':'011013'
         })
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))
 
    def getPage(self):
        request  = Request(
            url = self.loginUrl,
            data = str.encode(self.postdata))
        result = self.opener.open(request)
        #打印登录内容
        denglu_data = result.read()
        print(denglu_data)
        # return denglu_data