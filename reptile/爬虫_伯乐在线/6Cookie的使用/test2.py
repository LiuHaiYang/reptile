#保存Cookie到文件
from urllib.request import urlopen,HTTPCookieProcessor
import urllib
import http.cookiejar

#设置保存cookie的文件，同级目录下的cookie.txt
filename='cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)

#利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
handler = HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)


#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

##save方法
#官方解释如下：

# ignore_discard: save even cookies set to be discarded.

# ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists