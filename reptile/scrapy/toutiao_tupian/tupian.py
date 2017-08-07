#-*- coding: utf-8 -*-
import re
import urllib
import requests
import chardet
from multiprocessing.dummy import Pool

def urllink(link):
	html_1 = urllib.request.urlopen(link,timeout=120).read()
	encoding_dict = chardet.detect(html_1)
	web_encoding = encoding_dict['encoding']
	if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
		html = html_1
	else:
		html = html_1.decode('gbk','ignore').encode('utf-8')
	return html
linkl = "http://www.dazui88.com/tag/ligui/"
html = urllink(linkl)
plist =re.findall("<p>.*?</p>",html,re.S)
href = 'http://www.dazui88.com' + re.search('href="(.*?).html"',j).group(1)
picurl = re.findall('img alt.*?src="(.*?)"',html2)
for n in picurl:
	p +=1
	if not re.findall('http',n ,re.S):
		n = 'http://www.dazui88.com' + next
	print('正在下载图片，图片地址：' + n)
	retu = requests.get(n,stteam= True)
	picpath = unicode(r'C:\Users\samsung1\Desktop\scrapy\toutiao_tupian\%s\%s' % (label, str(p)) + '.jpg','utf-8')
	file = open(picpath,'wb')
	for chunk in retu.iter_content(chunk_size=1024*8):
		if  chunk:
			file.write(chunk)
			file.flush()
	file.close()
pool = Pool(4)
pool.map(downloadpic,plist)
pool.close()
pool.join()