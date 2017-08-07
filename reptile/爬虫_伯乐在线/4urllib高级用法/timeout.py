#urlopen方法了，第三个参数就是timeout的设置，
#可以设置等待多久超时，为了解决一些网站实在响应过慢而造成的影响

import urllib2
response = urllib2.urlopen('http://www.baidu.com', timeout=10)


response = urllib2.urlopen('http://www.baidu.com',data, 10)