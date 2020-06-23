import scrapy
from datetime import datetime
import time
import re
from datetime import timedelta

class SocialProgress(scrapy.Spider):
    # unique name of spider
    name = 'progress'

    # # Step 1. Start scrapy
    def start_requests(self):
        self.index = 0

        # main link for scrapping (all news)
        web = 'https://www.socialprogress.org/?tab=2&code=NLD'
        yield scrapy.Request(web, callback=self.get_links)

    # function  for fetching links
    def get_links(self, response):
        links = []
        base_link = 'https://www.socialprogress.org/?tab=2&code=NLD'

        # different code due to different html schema for first article
        links.append(base_link+response.xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div/ul[1]/li/div/a/@href').extract()[0])

        hrefs = response.xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/ul/li/div/div/a/@href').extract()
        for href in hrefs:
            links.append(base_link+href)
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_data)


    # Step 3. Function for extracting data from links

    def parse_data(self, response):
        
        # Construct all articles by parts
        paragraphs = []
        
        for paragraph in response.xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p/text()'):
            paragraphs.append(paragraph.get())

        yield {'header': response.xpath('//*[@id="content"]/div[1]/div[1]/div/div[2]/h1/text()').get().strip(), 
                'text': ' '.join(paragraphs)}