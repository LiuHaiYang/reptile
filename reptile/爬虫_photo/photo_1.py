#爬去js中图片   文字
import urllib.request
from bs4 import BeautifulSoup
import re
import json
import urllib.parse
import random
from collections import OrderedDict
def page_index():
    data = OrderedDict()
    data["action"]="show"
    data["__biz"]="MzA4MTc3NTQ3NA=="
    data["supervoteid"]=492693791
    data["uin"]=''
    data["key"]=''
    data["pass_ticket"]=''
    data["wxtoken"]=''
    data["mid"]=2650094317
    data["idx"]=1
    head = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
        "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.2372.400QQBrowser / 9.5.10548.400"
        ]
    header = {"user-agent": random.choice(head)}
    url = "http://mp.weixin.qq.com/mp/newappmsgvote?"+urllib.parse.urlencode(data)
    url_lib = urllib.request.urlopen(urllib.request.Request(url,headers=header)).read().decode("utf-8")
    picture = re.compile("var voteInfo=(.*?);",re.S)
    picture_img = re.search(picture,url_lib).group(1)
    picture_img_dict = json.loads(picture_img)

    for i in picture_img_dict.get("vote_subject"):
        for ii in i.get("options"):
            picture_title = ii.get("name")
            picture_url = ii.get("url")
            print("图片名字：%s"%picture_title)
            print("图片url：%s"%picture_url)
            urllib.request.urlretrieve(picture_url,"G:\photo\%s.jpg"%picture_title)
if __name__ == '__main__':
    page_index()