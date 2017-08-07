import scrapy

class StackoverflowSpider(scrapy.Spider):
	name = "Stackoverflow"
	start_urls = ["http://stackoverflow.com/questions?sort=votes"]
	
	
	def parse(self,response):
		for href in response.css('.question-summary h3 a::attr(href)'):##question-summary-11227809 > div.summary > h3 > a
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url,callback=self.parse_question)
			
	def parse_question(self,response):
		yield {
			'Title':response.css('h1 a::text').extract()[0],##question-header > h1 > a
			'Votes':response.css('.question .vote-count-post::text').extract()[0],
		}
