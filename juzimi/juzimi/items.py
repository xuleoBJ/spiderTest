# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JuzimiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    juzi = scrapy.Field()
    writer = scrapy.Field()
    article = scrapy.Field()
    xihua = scrapy.Field()
    pass
