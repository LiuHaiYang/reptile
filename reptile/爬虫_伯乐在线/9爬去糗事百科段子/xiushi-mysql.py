#-*-coding:utf-8 -*-
import urllib
from urllib.request import Request,urlopen
from urllib.error import URLError
from bs4 import  BeautifulSoup
import re
import pymysql
import datetime
import random
conn = pymysql.connect(host='127.0.0.1',
        user='root',passwd='843800695',db='pachong',charset='utf8')
cur = conn.cursor()

random.seed(datetime.datetime.now())

def store(name,p,pinglun):#'"+name+"','"+pass+"'
    # sql = "INSERT INTO xsbk (name,p,pinglun) VALUES ('"+name+"','"+p+"' + '"+pinglun+"')"
    # cur.execute(sql)#,(name,p,pinglun))
    cur.execute("INSERT INTO xsbk (name,p,pinglun) VALUES (\"%s\",\"%s\",%s)",(name,p,pinglun))
    cur.connection.commit()
    print("INSERT  OK!!!!!")

#糗事百科爬虫类

def get_info(page):
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
            store(name,p,pinglun)
    except URLError as e:
        if hasattr(e,"code"):
            print(e.code())
        if hasattr(e,"reason"):
            print(e.reason())


def info_all(strat,end):
    for i  in range(strat,end+1):
        get_info(i)

#输入起始页 和 终止页码
info_all(strat,end)
