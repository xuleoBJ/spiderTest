import scrapy
import random
import juzimi.items
class JuzimiSpider(scrapy.Spider):
    
    name = "juzimiSpider"
    allowed_domains = ["http://www.juzimi.com/"]

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]

    proxy_pool = ['https://127.0.0.1:8087']

    def start_requests(self):
        urls=["http://www.juzimi.com/ju/"+str(a) for a in range(45384,45400)]

        #urls=["http://www.baidu.com"]

        iNum = 0
        for url in urls:
            iNum = iNum + 1
            # if iNum % 100 == 0:
            #      print("记录"+str(iNum))
            ua = random.choice(self.user_agent_list)
            ip = random.choice(self.proxy_pool)
            yield scrapy.Request(url=url,callback=self.parse, 
                    headers={'User-Agent': ua},
                    meta={'proxy':ip},
                    dont_filter = True)
  
    def parse(self, response):
        #sel是页面源代码，载入scrapy.selector
        print (str(response.status)+" "+response.url)
        item = juzimi.items.JuzimiItem()
        if response.status == 200 :
            sel = response.selector
            juzi = sel.xpath('//title/text()').extract()
            item['juzi']= juzi
            writer = sel.xpath('////span[@class="field field-type-content-taxonomy field-field-oriwriter"]/a[@title and @ href]/text()')
            item['writer']= writer
            article = sel.xpath('//span[@class="field field-type-content-taxonomy field-field-oriarticle"]/a[@title and @ href]/text()')
            item['article']= article
            xihua = sel.xpath('//a[@title="查看心得/评论"]/text()')
            item['xihua']= xihua
            print(item)
            return item
                  