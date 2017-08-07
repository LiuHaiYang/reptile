# -*- coding：utf-8 -*-
import scrapy
class ZhilianZhaoPinSpider(scrapy.Spider):
	name = "zhilianzhaopin"
	start_urls = ["http://xiaoyuan.zhaopin.com/full/industry/160400"]
	
	
	def parse(self,response):
		for href in response.css('.searchResultJobinfo.fr p.searchResultJobName.clearfix a::attr(href)'):#div.searchResultJobinfo.fr > p.searchResultJobName.clearfix > a
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback=self.parse_question)
			
	def parse_question(self,response):
		yield {
			'Title':response.css('#JobName::text').extract(),
			'Address':response.css('#currentJobCity::text').extract(),
			'Date':response.css('#liJobPublishDate::text').extract(),
			'Body':response.css('.j_cJobDetail_tabSwitch_content > div > div > p::text').extract(),
		}
		
#运行及保存爬取数据方式
#scrapy runsplider    xxx.py -o xxx.csv