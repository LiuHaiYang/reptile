#从文件中获取Cookie并访问
from urllib.request import urlopen,HTTPCookieProcessor
import urllib
import http.cookiejar

filename = 'cookie_csdn.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
            'username':'qq_32230407',
            'password':'123456789**'
        })
data = str.encode(postdata)
#登录教务系统的URL
loginUrl = 'https://passport.csdn.net/account/login?ref=toolbar'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,data)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
OtherUrl = 'https://my.csdn.net/my/account/bind'
#请求访问成绩查询网址
result = opener.open(OtherUrl)
print(result.read().decode('utf-8'))

##原理
#创建一个带有cookie的opener，在访问登录的URL时，
#将登录后的cookie保存下来，然后利用这个cookie来访问其他网址
