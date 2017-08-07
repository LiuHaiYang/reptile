from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib
requset = urllib.request.Request('http://blog.csdn.net/cqcre')
try:
    urlopen(requset)
except URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
else:
    print("OK")