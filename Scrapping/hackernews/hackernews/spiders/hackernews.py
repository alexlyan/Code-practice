import scrapy
import datetime
import time

class hackerCrawler(scrapy.Spider):
    name = 'hackernews'
    

    # function 1
    def start_requests(self):
        self.index = 0

        base = 'https://news.ycombinator.com/'
        
        yield scrapy.Request(base, callback=self.parse)

    def parse(self, response):
        
        headers = response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/text()').getall()
        # xpath for text response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a')
        links = response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/@href').extract()  
        # response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/@href').extract()  
        points = list(map(lambda x: int(x.replace(' points', '')), response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/span/text()').getall())) 
        # response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/span/text()').getall() 
        comments = list(map(lambda x: int(x.replace('\xa0comments','')) if x != 'discuss' and x != '1\xa0comment' else 0, response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/a[3]/text()').getall()))
        # response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/a[3]/text()').getall()   
        for x in range(len(headers)):
            time.sleep(2)
            yield {
                'date': datetime.datetime.today(),
                'header': headers[x],
                'links': links[x],
                'views': points[x],
                'comments': comments[x]
            }