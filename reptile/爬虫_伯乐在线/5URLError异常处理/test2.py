from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib
requset = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urlopen(requset)
except URLError as e:
    print(e.reason)
except HTTPError as e:
    print (e.code)
else:
    print("OK")
