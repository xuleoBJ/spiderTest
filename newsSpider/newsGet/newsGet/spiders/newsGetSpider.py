import scrapy
##测试翻墙代理实现,获取新闻。
class newsSpider(scrapy.Spider):
    name = "newsGet"

    def start_requests(self):
        urls= ['http://www.times.com',
               'http://www.dwnews.com',]

        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback = self.parse)

    def parse(self,response):
        print(response.url)
        print(response.status)
        sel = response.selector
        print(sel.xpath("//h3").extract())
        

