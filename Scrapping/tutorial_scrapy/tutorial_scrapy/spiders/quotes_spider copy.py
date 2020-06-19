import scrapy
from datetime import date
import time
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "kak"
    
    start_urls = ['https://kaktus.media/?date={date.today().isoformat()}&lable=8&order=main']

    # main function for extracting data
    def parse(self, response):

        time.sleep(2)

        yield {
            'time': datetime.strptime(response.xpath('/html/body/div[2]/div[5]/div/div/div/div/div[2]/time/@datetime').extract()[0],'%Y-%m-%dT%H:%M:%S%z'),
            'header': response.xpath('/html/body/div[2]/div[5]/div/div/div/h1/span[1]/text()').get(),
            # 'text': article.xpath('div[2]/a/span[1]/text()').get(),
            'views': response.xpath("/html/body/div[2]/div[5]/div/div/div/div/div[1]/span/text()").get().strip(), ###
            'comment': response.xpath("/html/body/div[2]/div[5]/div/div/div/div/div[1]/span[2]/text()").get().strip()
        }
