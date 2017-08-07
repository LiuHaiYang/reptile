import requests
from bs4 import BeautifulSoup
import time
import os
import re
import urllib.request
import random
from collections import OrderedDict
header = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"  ,
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
        "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.2372.400QQBrowser / 9.5.10548.400"
]

def main_html(url,head):
    #使用代理ip
    proxy_handler = urllib.request.ProxyHandler({'post': '223.18.181.240:8380'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
    urllib.request.install_opener(opener)
    #随机头文件
    hrader = {"User-Agent":random.choice(head)}
    main_url = urllib.request.Request(url,headers=hrader)
    urll = urllib.request.urlopen(main_url).read()
    #用BeautifulSoup
    bs = BeautifulSoup(urll,"html.parser")
    # print(bs)
    pages = OrderedDict()
    bs_s = bs.find_all("a", href=re.compile("http://www.mzitu.com/([0-9]+)"))
    # print(bs_s)
    for i in bs_s:
        url_name = i.get_text()
        pages[url_name] = i.attrs["href"]
    print("去重结束")
    print(pages)
    return pages
def download(pages,heade):

    for i in pages.values():
        q = 1
        header = {"User-Agent": random.choice(heade)}
        while q>0:
            url_list = i+"/"+"%d"%q
            # print(url_list)
            # break
            url = urllib.request.Request(url_list,headers=header)
            url_re = urllib.request.urlopen(url).read()
            bs = BeautifulSoup(url_re,"html.parser")
            bs_page = bs.find("div",{"class":"pagenavi"}).find_all("a")
            # print(bs_page[-2].get_text())#总页数
            page_all = int(bs_page[-2].get_text())
            bsj_a = bs.find("div",{"class":"main-image"}).img
            # print(bsj_a)

            # print(bsj_a.attrs["alt"]+":"+bsj_a.attrs["src"])
            try:
                # time.sleep(3)
                path = "D:\meinv1\\%s"%bsj_a.attrs["alt"]+"%d"%q+".jpg"
                # print(path)
                if not os.path.exists(path):
                    urllib.request.urlretrieve(bsj_a.attrs["src"],path)
                    print("下载成功:"+bsj_a.attrs["alt"]+":"+bsj_a.attrs["src"])
                q+=1

                if q>page_all:
                    q=0
            except urllib.error.URLError as e:
                print(e)
if __name__=="__main__":

    url = "http://www.mzitu.com/all"
    pages = main_html(url,header)
    download(pages,header)
    # main_html(url,header)