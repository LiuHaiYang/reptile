# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_list_title = scrapy.Field()
    book_number = scrapy.Field()
    book_url = scrapy.Field()
    book_list_author = scrapy.Field()
    book_list_date = scrapy.Field()
    book_list_summary = scrapy.Field()
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_summary = scrapy.Field()