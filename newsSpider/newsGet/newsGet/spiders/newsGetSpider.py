import scrapy

class newsSpider(scrapy.Spider):
    name = "newsGet"

    def start_requests(self):
        urls= ['http://www.dwnews.com']

        for url in urls:
            yield scrapy.Request(url=url,callback = self.parse)

    def parse(self,response):
        print(response.status)
