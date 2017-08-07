#test1
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
# response = urlopen("http://www.baidu.com")
# print(response.read())

#test2
#POST  和 GET  数据传送

#POST 
# values = {"username":"843800695","password":""}
# data = urllib.parse.urlencode(values) 
# binary_data = str.encode(data)
# url = "https://http://qzone.qq.com/"
# request = urllib.request.Request(url,binary_data)
# html =urlopen(request)
# bsobj = BeautifulSoup(html)
# # print(response.read())
# print(bsobj.title)

#POST
values = {}
values['username'] = "qq_32230407"
values['password'] = ""
data = urllib.parse.urlencode(values) 
data = str.encode(data)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urlopen(request)
print(response.read())
txt = b"\xe5\xb8\x90\xe5\x8f\xb7\xe7\x99\xbb\xe5\xbd\x95"
txt1 = bytes.decode(txt)
print(txt1)