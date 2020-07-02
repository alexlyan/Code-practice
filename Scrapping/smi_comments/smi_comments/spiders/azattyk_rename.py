import scrapy
from datetime import datetime
import time
import selenium
from selenium import webdriver

class AzattykComment(scrapy.Spider):

    # unique name
    name = 'azattykcomment'

    def start_requests(self):
            web = 'https://rus.azattyk.org/z/4795'

            yield scrapy.Request(web, callback=self.get_links)

    def get_links(self, response):
        links = []
        base_link = 'https://rus.azattyk.org'
        browser = webdriver.Safari()
        browser.get('https://rus.azattyk.org/z/4795')

        elem = browser.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[1]/div[2]/p/a/')
        elem.click()
        time.sleep(0.2)

        # different code due to different html schema for first article
        links.append(base_link+response.xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div/ul[1]/li/div/a/@href').extract()[0])

        hrefs = response.xpath('/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/ul/li/div/div/a/@href').extract()
        for href in hrefs:
            links.append(base_link+href)
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_data)

# response.xpath('//*[@id="comments"]/div/div/div[2]') 
    def parse(self, response):

        yield {
            'link': response.url
        }

    

