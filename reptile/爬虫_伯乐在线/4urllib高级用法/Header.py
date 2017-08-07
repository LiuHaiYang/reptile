from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

url = 'https://passport.csdn.net/account/login?ref=toolbar'
user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'  
values = {'username' : 'qq_32230407',  'password' : '123456789**' }  
headers = { 'User-Agent' : user_agent }  
values = str.encode(values)
data = urllib.parse.urlencode(values)  
request = urllib.request.Request(url, data, headers)  
response = urlopen(request)  
page = response.read()