import scrapy
from time import sleep

class kloop_crawler(scrapy.Spider):
	name = 'kloop'

	def start_requests(self):

		web = 'https://kloop.kg/news/'

		yield scrapy.Request(url=web, callback=self.links)


	def links(self, response):
		all_links = []

		l_xpath = '//section/div/div/div[1]/div/div/div/div/div/article[{}]/div/h3/a/@href'

		for i in range(1, 30):
			link = response.xpath(l_xpath.format(i)).get()
			if link is None:
				break
			all_links.append(link)
			sleep(2)

		for l in all_links:
			yield scrapy.Request(url=l, callback=self.data_extracting)
			sleep(1)


	def data_extracting(self, response):
    		
		header = '//div/article/div[1]/div/div/header/h1/text()'
		body = '/html/body/div[6]/div[2]/div[1]/article/div[2]/div[1]/div[1]/div[@class="td-post-content"]/div[2]/div[1]/div[1]/div[1]/p[{}]/text()'
		time = '//article/div[1]/div/div/header/div/span/time/@datetime'


		article =[]

		for i in range(1, 20):

			article_body = response.xpath(body.format(i))
			if article_body is None:
				break
			article.append(article_body.get())
			sleep(1)

		yield {
			'url': response.url,
			'header': response.xpath(header).get(),
			'time': response.xpath(time).get()[:10],
			'topic': ' '.join(article)
		}
