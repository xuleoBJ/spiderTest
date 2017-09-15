# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
#Item Loaders提供了一种便捷的方式填充抓取到的 :Items
from scrapy.contrib.loader import ItemLoader, Identity
from meizitu.items import MeizituItem
import os
from datetime import datetime 

class MeiziSpider(scrapy.Spider):
    name = "meiziXL"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://www.meizitu.com/a/more_1.html',
    )
    img_urls = []
    def parse(self, response):
        #sel是页面源代码，载入scrapy.selector
        sel = response.selector
        #每个连接，用@href属性
        for link in sel.xpath('//h3/a/@href').extract():
            #请求=Request(连接，parese_item)
            print (link)
            yield scrapy.Request(link, callback=self.parse_item ,dont_filter = True)

    def makeTodayDirStr(self,dirName):
        strToday = datetime.now().strftime("%Y%m%d")
        strPath = "e:/webScrapy/"+dirName
        if not os.path.exists(strPath):
            os.makedirs(strPath)
        return strPath

    
    def parse_item(self, response):
        item=MeizituItem()
        subSel = response.selector
        #每个连接，用@href属性
        titleDir = subSel.xpath('//h2/a/text()').extract()[0]
        
        dirToday = self.makeTodayDirStr(titleDir)
        for jpgLink in subSel.xpath('//img/@src').extract():
            #请求=Request(连接，parese_item)
            if "mm.chinasareview.com/wp-content" in jpgLink:
                self.img_urls.append(jpgLink)
                print (jpgLink)
       
        item['name'] = titleDir
        item['url'] = response.url
        item['image_urls'] = self.img_urls