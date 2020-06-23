import scrapy
from datetime import date
import time
from datetime import datetime
import re

class QuotesSpider(scrapy.Spider):
    name = "24"
    
    def start_requests(self):
        self.index = 0

        start_urls = 'https://24.kg/'

    # access to website
        yield scrapy.Request(url=start_urls, callback=self.get_links)

    #function for taking links
    def get_links(self, response):
        links = []

        for link in response.xpath('/html/body/div[4]/div[5]/div[1]/div/div/div[2]/div/div[2]/a/@href'):
            time.sleep(1)

            href = 'https://24.kg'+link.get()
            links.append(href)
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse) 

    # main function for extracting data
    def parse(self, response):

        # part for parsing paragraphs
        paragraphs = []
        
        
        if response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[3]/p'):
            xpath_paragraph = response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[3]/p')
        elif response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[4]/p'):
            xpath_paragraph = response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[4]/p')
        else:
            xpath_paragraph = response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[3]/div[2]/p')

        # get numbers of paragraphs
        len_pars = len(xpath_paragraph)

        for par in range(len_pars):
            # find all patterns and join with ' ' and replace all bytecode parts to space
            paragraph = ' '.join(re.findall(r'>(.*?)<', xpath_paragraph[par].get())).replace('\xa0', ' ')
            paragraphs.append(paragraph)
        
        # parsing time 
        time.sleep(2)

        # parsing time
        if response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[3]/div/span[1]/@content'):
            time_date = datetime.strptime(response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[3]/div/span[1]/@content').extract()[0][:10], '%Y-%m-%d')
        else:
            time_date = datetime.strptime(response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[1]/div[2]/span[1]/@content').extract()[0][:10], '%Y-%m-%d')


        # parsing view number
        if response.xpath('/html/body/div[4]/div[2]/div[1]/div[1]/div[5]/div[1]/text()[4]').get():
            views = int(re.findall(r'(\d+)', response.xpath('/html/body/div[4]/div[2]/div[1]/div[1]/div[5]/div[1]/text()[4]').get())[0])
        else:
            views = int(re.findall(r'(\d+)', response.xpath('/html/body/div[4]/div[2]/div[1]/div[1]/div[4]/div[1]/text()[4]').get())[0])

        yield {
            'url': response.url,
            'date': time_date,
            'topic': response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/div[1]/div[1]/a/text()').get().strip(),
            'header': response.xpath('//*[@id="content-wrapper"]/div[1]/div[1]/h1/text()').get().replace('\xa0', ' '),
            'content': ' '.join(paragraphs),
            'views': views
        }
