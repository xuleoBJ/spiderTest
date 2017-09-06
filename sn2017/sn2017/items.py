# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item,Field

class Sn2017Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    pass

class snItem(scrapy.Item):
    mingcheng = Field()
    dizhi = Field()
    pingjia = Field()
    stars = Field()
    fuwutaidu = Field()
    shangjiahuanjing = Field()
    jiage = Field()
    qqNum = Field()
    weChatNum = Field()
    telNum = Field()
    pass