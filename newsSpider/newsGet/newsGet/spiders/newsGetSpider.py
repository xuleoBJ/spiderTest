import scrapy

class newsSpider(scrapy.Spider):
    name = "newsGet"

    def start_requests(self):
        urls= ['http://www.yahoo.com',
               "http://www.dwnews.com"]

        for url in urls:
            print(url)
            yield scrapy.Request(url=url,callback = self.parse)

    def parse(self,response):
        print(response.url)
        print(response.status)
