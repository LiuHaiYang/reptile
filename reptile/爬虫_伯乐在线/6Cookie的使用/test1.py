#获取Cookie保存到变量
from urllib.request import urlopen,HTTPCookieProcessor
import urllib
from urllib.error import URLError, HTTPError
import http.cookiejar

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

r = opener.open('http://www.baidu.com')
# print(r.read().decode('utf-8'))
for i in cookie:
    print( i.name + '  = ' +i.value)

# #结果
# BAIDUID  = C99594FADF3A069ED9FC7EAB82B6F5BB:FG=1
# BIDUPSID  = C99594FADF3A069ED9FC7EAB82B6F5BB
# H_PS_PSSID  = 22164_1420_21088_18560_17001_20927
# PSTM  = 1491394718
# BDSVRTM  = 0
# BD_HOME  = 0

