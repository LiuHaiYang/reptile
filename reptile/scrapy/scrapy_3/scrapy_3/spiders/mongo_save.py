# -*- coding: utf-8 -*-
import scrapy
from scrapy_3.items import Scrapy3Item

class MongoSaveSpider(scrapy.Spider):
    name = "mongo_save"
    allowed_domains = [" "]
    start_urls = ['http://www.book110.com/981.html']

    def parse(self, response):
        book_list_group = response.xpath('li:nth-child h3 a::attr(href)')
        for book_list in book_list_group:
        	item = Scrapy3Item()
        	item['book_list_title'] = book_list.xpath('li:nth-child h3 a::text').extract()[0]
        	# item['book_author'] = book_list.xpath('span:nth-child a::text').extract()[0]
        	book_list_url = book_list.xpath('li:nth-child h3 a::attr(href)').extract()[0]
        	yield scrapy.Request(self.url + book_list_url, 
        		callback=self.parse_book_list_detail,meta={'item':item})

    def parse_book_list_detail(self , response):
    	item = response.meta['item']
    	summary = response.xpath('#iframeContent::text').extract()
    	item['book_list_summary'] = '\n'.join(summary)	
    	yield item
