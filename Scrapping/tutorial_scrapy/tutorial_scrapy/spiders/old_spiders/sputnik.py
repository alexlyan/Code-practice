import scrapy
from datetime import date
import time
from datetime import datetime
import re

class QuotesSpider(scrapy.Spider):
    name = "sputnik"
    
    def start_requests(self):
        self.index = 0

        start_urls = 'https://ru.sputnik.kg/news/' # changed to dynamic dates

    # access to website
        yield scrapy.Request(url=start_urls, callback=self.get_links)

    #function for taking links
    def get_links(self, response):
        links = []

        for link in response.xpath('//*[@id="rubric-major"]/div[1]/ul/li'):
            time.sleep(2)

            href = link.xpath('div[2]/h2/a/@href').get()
            links.append('https://ru.sputnik.kg'+ href)
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse) 

    # main function for extracting data
    def parse(self, response):
        

        # Parse Content
        paragraphs = [] 

        xpath_paragraph = response.xpath('/html/body/div[1]/div[7]/div/div[1]/div/div[4]/p') 

        # get numbers of paragraphs
        len_pars = len(xpath_paragraph)

        for par in range(len_pars):
            # find all patterns and join with ' '
            paragraph = ' '.join(re.findall(r'>(.*?)<', xpath_paragraph[par].get()))
            paragraphs.append(paragraph)

        # Parsing datetime
        date_time = datetime.strptime(response.xpath('/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[1]/time[1]/@datetime').extract()[0][:10], '%Y-%m-%d')
        
        # Parsing views
        try:                                                                    # \/ different index
            if response.xpath('/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[4]/span[1]/text()').get():
                views = response.xpath('/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[4]/span[1]/text()').get()
            elif response.xpath("/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[2]/span[1]/text()").get():
                views = response.xpath("/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[2]/span[1]/text()").get()
            else:
                views = response.xpath("/html/body/div[1]/div[7]/div/div[1]/div/div[1]/div[3]/span[1]/text()").get()
        except TypeError:
            '-9999'

        time.sleep(1)

        yield {
            'url': response.url,
            'date': date_time,
            'header': response.xpath('/html/body/div[1]/div[6]/div/div/div[1]/h1/text()').get(),
            'topic': response.xpath('/html/body/div[1]/div[7]/div/div[1]/div/div[1]/a/text()').get(),
            'content': ' '.join(paragraphs),
            'views': views
        }
