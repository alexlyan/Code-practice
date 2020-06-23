import scrapy
from datetime import date
import time
from datetime import datetime

class QuotesSpider(scrapy.Spider):
    name = "kaktus"
    
    def start_requests(self):
        self.index = 0

        start_urls = f'https://kaktus.media/?date={date.today().isoformat()}&lable=8&order=main#paginator' # changed to dynamic dates

    # access to website
        yield scrapy.Request(url=start_urls, callback=self.get_links)

    #function for taking links
    def get_links(self, response):
        links = []

        for link in response.xpath('/html/body/div[2]/div[6]/div/div/div[1]/ul/li[2]/ul/li'):
            time.sleep(2)

            href = link.xpath('div/a/@href').get()
            links.append(href)
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse) 

    # main function for extracting data
    def parse(self, response):

        paragraphs = [] 
        for paragraph in response.xpath('/html/body/div[2]/div[5]/div/div/div/div[4]/div[4]/p/text()'):  
            paragraphs.append(paragraph.get())

        time.sleep(1)

        yield {
            'url': response.url,
            'date': datetime.strptime(response.xpath('/html/body/div[2]/div[5]/div/div/div/div/div[2]/time/@datetime').extract()[0],'%Y-%m-%dT%H:%M:%S%z'),
            'topic': response.xpath('/html/body/div[2]/div[5]/div/div/div/p/a/span/text()').get(),
            'header': response.xpath('/html/body/div[2]/div[5]/div/div/div/h1/span[1]/text()').get(),
            'content': ' '.join(paragraphs),
            'views': response.xpath("/html/body/div[2]/div[5]/div/div/div/div/div[1]/span/text()").get().strip(), ###
            # 'comment': response.xpath("/html/body/div[2]/div[5]/div/div/div/div/div[1]/span[2]/text()").get().strip()
        }
