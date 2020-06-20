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
        
        # nums_articles = response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/text()').getall()
        # # xpath for text response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a')
        # links = response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/@href').extract()  
        # # response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/@href').extract()  
        # points = list(map(lambda x: int(x.replace(' points', '')), response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/span/text()').getall())) 
        # # response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/span/text()').getall() 
        # comments = list(map(lambda x: int(x.replace('\xa0comments','')) if x != 'discuss' and x != '1\xa0comment' else 0, response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/a[3]/text()').getall()))
        # # response.xpath('/html/body/center/table/tr[3]/td/table/tr/td[@class="subtext"]/a[3]/text()').getall()   
        # for x in range(len(headers)):
        #     time.sleep(2)
        #     yield {
        #         'date': datetime.datetime.today(),
        #         'header': headers[x],
        #         'links': links[x],
        #         'views': points[x],
        #         'comments': comments[x]
        #     }

    # test code
        # path to arrowbutton
        nums_articles = response.xpath('/html/body/center/table/tr[3]/td/table/tr[@class="athing"]/td/a/text()').getall()

        #xpaths to data
        xpath_main = '/html/body/center/table/tr[3]/td/table/tr[{}]/td[2]/center/a/div/@class'
        header_xpath = '/html/body/center/table/tr[3]/td/table/tr[{}]/td/a/text()'
        link_xpath = '/html/body/center/table/tr[3]/td/table/tr[{}]/td/a/@href'
        views_xpath = '/html/body/center/table/tr[3]/td/table/tr[{}]/td[@class="subtext"]/span/text()'
        comments_xpath = '/html/body/center/table/tr[3]/td/table/tr[{}]/td[@class="subtext"]/a[3]/text()'
        # lists
        headers = []
        links = []
        views = []
        comments = []

        # function for comments; replace string and convert into int
        func_replacement = lambda x: int(x.replace('\xa0comments','')) if x != 'discuss' and x != '1\xa0comment' else 0


        for i in range(1, len(nums_articles)*3):
            time.sleep(2)
            # if there is arrow button append to lists
            if response.xpath(xpath_main.format(i)).extract():
                headers.append(response.xpath(header_xpath.format(i)).get())
                links.append(response.xpath(link_xpath.format(i)).get())
                views.append(int(response.xpath(views_xpath.format(i+1)).get().replace(' points', '')))
                comments.append(func_replacement(response.xpath(comments_xpath.format(i+1)).get()))
            else:
                pass

        for x in range(len(headers)):
                time.sleep(2)
                yield {
                    'date': datetime.datetime.today(),
                    'header': headers[x],
                    'links': links[x],
                    'views': views[x],
                    'comments': comments[x]
                }