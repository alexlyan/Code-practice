import scrapy
from datetime import datetime
import time
import re
from datetime import timedelta

class AzattykSpider(scrapy.Spider):
    # unique name of spider
    name = 'azatyk'

    # # Step 1. Start scrapy
    def start_requests(self):
        self.index = 0

        # main link for scrapping (all news)
        web = 'https://rus.azattyk.org/z/4795'
        yield scrapy.Request(web, callback=self.get_links)

    # function  for fetching links
    def get_links(self, response):
        links = []
        base_link = 'https://rus.azattyk.org'

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

        # fetching date and time
        # dict of months
        months = {'января': 1,
          'февраля': 2,
          'марта': 3,
          'апреля': 4,
          'мая': 5,
          'июня': 6,
          'июля': 7,
         'августа': 8,
         'сентября': 9,
         'октярбря': 10,
         'ноября': 11,
         'декабря': 12}

         # parsing date and time
        date_time = response.xpath('//*[@id="content"]/div[1]/div[1]/div/div[3]/div/div/span/time/text()').get().strip()

        # if publication was recently posted in mins ago "минуты", we substract mins from now time
        if re.search(r'минут(ы)', date_time):
            mins = re.findall(r'\w+', date_time)
            date = datetime.now() - timedelta(minutes=int(mins[0]))
        # if publication was recently posted in hour(s) ago "часы", we substract hours from now time
        elif re.search(r'часа', date_time):
            hours = re.findall(r'\w+', date_time)
            date = datetime.now() - timedelta(hours=int(hours[0]))
        # else return time published
        else:
            m, d, y = date_time.replace(',', '').split()
            date = datetime.strptime(f'{y}-{months[m]}-{d}','%Y-%m-%d')

        # Parsing Topic of artictle
        topic = response.xpath('//*[@id="content"]/div[1]/div[1]/div/div[1]/div/a/text()').get()       
        
        time.sleep(2)

        yield {
                'url': response.url,
                'date': date,
                'header': response.xpath('//*[@id="content"]/div[1]/div[1]/div/div[2]/h1/text()').get().strip(),
                'topic': topic,
                'content': ' '.join(paragraphs),
                'views': 0
        }