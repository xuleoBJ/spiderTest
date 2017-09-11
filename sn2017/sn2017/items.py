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
    mingcheng = Field()  ##名称
    dizhi = Field()    ##地址
    pingjia = Field()  ##评价
    stars = Field()    ##星级
    fuwutaidu = Field()  ##服务态度
    shangjiahuanjing = Field() ##商家环境
    jiage = Field()  ##价格
    jishiNum = Field() ##技师数目
    qqNum = Field()  ##qq号码
    weChatNum = Field() #微信
    telNum = Field()  ## 电话号码
    jieshao = Field() ##商户介绍
    pass