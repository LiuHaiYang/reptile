# -*- coding: utf-8 -*-
from urllib import request
import re
import os,glob
import xlwt

book = xlwt.Workbook()
sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
path = 'C:\\Users\\samsung1\\Desktop\scrapy\\toutiao_zhilian'
os.chdir(path)
result11=[]
result21=[]
result31=[]
result41=[]
result51=[]
for  k in range(1,11):
	html = request.urlopen("http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p="+str(k)).read()#¶ÁÈ¡ÍøÒ³Ô´´úÂëÄÚÈİ
	pat1 = 'onclick="submitLog.*?">(.*?)</a>'
	pat2 = '<td class="gsmc"><a href="https://ask.hellobi.com/(.*?)" target='
	pat3 = '<td class="zwyx">(.*?)</td>'
	pat4 = '<td class="gzdd">(.*?)</td>'
	pat5 = 'target="_blank">(.*?)<'
	result1 = re.compile(pat1).findall(str(html,"utf-8"))
	result2 = re.compile(pat2).findall(str(html,"utf-8"))
	result3 = re.compile(pat3).findall(str(html,"utf-8"))
	result4 = re.compile(pat4).findall(str(html,"utf-8"))
	result5 = re.compile(pat5).findall(str(html,"utf-8"))
	result11.extend(result1)
	result21.extend(result2)
	result31.extend(result3)
	result41.extend(result4)
	result51.extend(result5)
	j = 0
for i in range(0,len(result11)-1):
	try:
		zhiwei = result11[i]
		wangzhi = result21[i]
		gongzi = result31[i]
		gongzuodidian = result41[i]
		gongsimingcheng = result51[i]
		sheet.write(i + 1, j, zhiwei)
		sheet.write(i + 1, j + 1, wangzhi)
		sheet.write(i + 1, j + 2, gongzi)
		sheet.write(i + 1, j + 3, gongzuodidian)
		sheet.write(i + 1, j + 4, gongsimingcheng)
	except Exception as e:
		print('error:' + str(e))
	continue
book.save('C:\\Users\\samsung1\\Desktop\\scrapy\\toutiao_zhilian\\shujufenxishi.xls')	