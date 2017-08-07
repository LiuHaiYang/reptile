from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib
requset = urllib.request.Request('http://www.xxxxx.com')
try:
    urlopen(requset)
except URLError as e:
    print (e.reason)
