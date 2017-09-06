import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import snItem

class FWSpider(scrapy.Spider):
    name = "sn2017"
    allowed_domains = ["http://www.sizubeijing.com/"]
   
    def start_requests(self):
        urls=[ "http://www.sizubeijing.com/item.php?act=list&catid=2",
        "http://www.sizubeijing.com/item.php?act=list&catid=1&aid=2.php",
        "http://www.sizubeijing.com/item.php?act=list&catid=1&aid=3",
        "http://www.sizubeijing.com/item.php?act=list&catid=1&aid=4",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
        sel = response.selector
        print(response.url)
        urlList = sel.xpath('//div[@class="tit"]/a/@href').extract()
        # print (urlList)
        for subUrl in urlList:   
            subUrl ="http://www.sizubeijing.com"+subUrl
            print (subUrl)
            yield scrapy.Request(url=subUrl, callback=self.parse_item,dont_filter = True)

        # subUrl = Selector(response=response).xpath('//div[@class="tit"]/a/@href').extract()
        
        # subUrl =response.urljoin(subUrl)
        # print (subUrl)

        # page = response.url.split("/")[-2]
        # filename = 'sn-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

       # return [Request(subUrl, callback=self.parse_item)]
      

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
         dizhi = response.selector.xpath('//div/p[@class="expand-info"]/span/text()') \
         .extract()
         print(dizhi)
         
         lianxi = response.selector.xpath('//div/p[@class="expand-info tel"]/span/text()') \
         .extract()
         print(lianxi)
         item = snItem()
         item['mingcheng'] = ""
         item['didian'] = dizhi
         item['telNum'] = lianxi
         return [item]
      