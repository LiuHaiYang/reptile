# -*- coding: utf-8 -*-
import scrapy
from scrapy_2.items import *

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = ['http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
				'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/']

    def parse(self, response):
#读取html
#        file_name = response.url.split('/')[-2] + ".html"
#		 with open(file_name,'wb') as fp:
#			fp.write(response.body)
		lis = response.xpath('')
		for li in lis:
			item = TutorialItem()
			item['title'] = li.xpath('').extract()
			item['title'] = li.xpath('').extract()
			item['title'] = li.xpath('').extract()
			
		
		
