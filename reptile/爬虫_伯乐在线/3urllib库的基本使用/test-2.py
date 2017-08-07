#GET
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

values={}
values['username'] = "qq_32230407"
values['password'] = "123456789**"
data = urllib.parse.urlencode(values) 
url = "https://passport.csdn.net/account/login?ref=toolbar"
geturl = url + "?"+data
request = urllib.request.Request(geturl)
response = urlopen(request)
print (response.read())
txt = b"\xe5\xb8\x90\xe5\x8f\xb7\xe7\x99\xbb\xe5\xbd\x95"
txt1 = bytes.decode(txt)
print(txt1)