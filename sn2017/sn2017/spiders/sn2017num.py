import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import snItem

class FWSpider(scrapy.Spider):
    name = "sn2017num"
    allowed_domains = ["http://www.sizubeijing.com/"]
   
    def start_requests(self):
        urls=["http://www.dushitiyan.com/ViewShop.aspx?id="+str(a) for a in range(0,2000)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter = True)


    def parse(self, response):
         mingcheng = response.selector.xpath('//div/h1[@class="shop-name"]/text()') \
         .extract()
         print(mingcheng)
         pingjia = response.selector.xpath('//div/div[@class="brief-info"]/span/text()') \
         .extract()
         print(pingjia)
         dizhi = response.selector.xpath('//div/p[@class="expand-info address"]/span/text()') \
         .extract()
         print(dizhi)
         lianxi = response.selector.xpath('//div/p[@class="expand-info tel"]/span/text()') \
         .extract()
         print(lianxi)
         item = snItem()
         item['mingcheng'] = mingcheng
         item['dizhi'] = dizhi
         item['stars'] = pingjia
         item['telNum'] = lianxi
         item['pingjia'] = pingjia
         with open('infor.txt', 'a') as f:
             if item['mingcheng']!='':
                f.write('名称: {0}, 地址: {1},联系方式: {2}, 评价: {3}\n'.format( \
                item['mingcheng'], item['dizhi'], item['telNum'],item['pingjia'] ))
         return [item]
      