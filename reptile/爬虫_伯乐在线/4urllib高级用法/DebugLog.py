##通过下面的方法把 Debug Log 打开，
#这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用，
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')