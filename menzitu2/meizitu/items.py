# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    #定义item对象,包含如下
    url = scrapy.Field()
    name = scrapy.Field()
    image_urls = scrapy.Field()
