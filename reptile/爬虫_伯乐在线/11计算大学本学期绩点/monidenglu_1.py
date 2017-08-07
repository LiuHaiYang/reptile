# -*- coding:utf-8 -*-
import re
import requests
import json
from urllib.request import urlopen,HTTPCookieProcessor,Request,build_opener
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError
#河北工程大学绩点运算
class SDU:
 
    def __init__(self):
        self.loginUrl = 'http://219.148.85.172:9380/loginAction.do'
        self.cookies = http.cookiejar.CookieJar()

        self.postdata = urllib.parse.urlencode({
            'zjh':'140212130',
            'mm':'011013',
         })
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        headers={'User-Agent':user_agent}
        self.opener = build_opener(HTTPCookieProcessor(self.cookies))

 
    def getPage(self):
        request  = Request(
            url = self.loginUrl,
            data = str.encode(self.postdata))
        result = self.opener.open(request)
        #打印登录内容
        denglu_data = result.read()
        # print(denglu_data.decode('gbk'))
        bsObj = BeautifulSoup(denglu_data)
        all_url_main = bsObj.findAll('frame') 
        main_url=all_url_main[1]
        url_l = str(main_url)[93:112]
        url = 'http://219.148.85.172:9380' +url_l
        url_kk = 'http://219.148.85.172:9380/menu/mainFrame.jsp'
        print(url)
        s= requests.Session()
        s.get(url_kk)
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        headers={'User-Agent':user_agent}
        # print(url)
        # http://219.148.85.172:9380/menu/mainFrame.jsp
        try:
            # html = self.opener.open(all_url_body)
            # bsObj = BeautifulSoup(html)
            result = requests.post(url_kk,data=json.dumps(self.postdata),headers=headers)
            # result = self.opener.open(self.gradeUrl)   
        except URLError as e:
            print(e.reason)
        except HTTPError as e:
            print (e.code)
        else:
            print(result.content.decode('gbk'))
 
sdu = SDU()
sdu.getPage()
# sdu.get_all_url()
