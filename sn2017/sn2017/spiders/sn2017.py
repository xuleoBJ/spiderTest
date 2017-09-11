import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import snItem

class FWSpider(scrapy.Spider):
    name = "sn2017"
    allowed_domains = ["http://www.sizubeijing.com/"]
   
    def start_requests(self):
        urls=["http://www.dushitiyan.com/ShopList.aspx?remen=1&district="+str(a) for a in range(49,50)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        sel = response.selector
        print(response.url)
        urlList = sel.xpath('//div[@class="tit"]/a/@href').extract()
        # print (urlList)with open('log.txt', 'a') as f:
        txtUrlList = open('_urlList.txt', 'w')
        for subUrl in urlList:
            subUrl ="http://www.dushitiyan.com"+subUrl
            txtUrlList.write(subUrl+'\n')
        txtUrlList.close()
        for subUrl in urlList:   
            subUrl ="http://www.dushitiyan.com"+subUrl
            print (subUrl)
            yield scrapy.Request(url=subUrl, callback=self.parse_item,dont_filter = True)

            ## 翻页查询
            # yield scrapy.FormRequest.from_response(response=response,
            #                                    clickdata=self.parse_item,
            #                                    dont_filter = True ,
            #                                    formdata={'__EVENTTARGET': 'ctl00$Content$AspNetPager1',
            #                                     '__EVENTARGUMENT': [str(i) for i in range(5)]})
       
      

    def parse_item(self, response):
    # item['key'] = value
        #  print("ok")
        #  print(response.url)
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
             f.write('名称: {0}, 地址: {1},联系方式: {2}, 评价: {3}\n'.format( \
             item['mingcheng'], item['dizhi'], item['telNum'],item['pingjia'] ))
         return [item]
      