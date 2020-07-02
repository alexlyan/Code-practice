import scrapy
from datetime import datetime
import time
import re
from datetime import timedelta
from scrapy_splash import SplashRequest
import pandas as pd

class SocialProgress(scrapy.Spider):
    # unique name of spider
    name = 'progress'

    # # Step 1. Start scrapy
    def start_requests(self):
        self.index = 0
        # df = pd.read_csv('iso3.csv')
        # iso3_list = df['iso_alpha'].to_list()
        iso3_list = ['CHN', 'IND', 'USA', '333']
        # main link for scrapping (all news)
        base = 'https://www.socialprogress.org/?tab=2&code={}'
        links = [f'https://www.socialprogress.org/?tab=2&code={x}' for x in iso3_list]
        for link in links:
            time.sleep(1)
            yield SplashRequest(url=link, callback=self.parse_data, args={'wait': 10})


    # Step 3. Function for extracting data from links

    def parse_data(self, response):
        

        yield {
            'country_name': response.xpath('/html/body/div/main/div/div[2]/div[1]/div[1]/h2/text()').get(), 
            'world_position': int(response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[2]/span[3]/text()').get()),
            'Social_Progress_Index': float(response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[2]/span[2]/text()').get()),
            'GDP_PPP_pc': int(response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/span[2]/text()').get().replace('$', '').replace(',', '')),
            'GDP_PPP_pc_position': int(response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/span[3]/text()').get()),
            'Basic_human_needs': int(response.xpath()),
            'Basic_human_needs_rank':int(response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/div/div[2]/span[3]/text()').get()),
            'Basic_Medical_Care': response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[1]/li[1]/span[2]/text()').get(),
            'Basic_Medical_Care_rank:': response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[1]/li[1]/span[3]/text()').get(),
            'Water_and_Sanitation': response.xpath(''),
            'Water_and_Sanitation_rank': response.xpath(''),
            'Shelter' response.xpath(''):,
            'Shelter_rank': response.xpath(''),
            'Personal_safety': response.xpath(''),
            'Personal_safety_rank': response.xpath(''),
            'Foundations_of_Wellbeing': response.xpath(''),
            'Foundations_of_Wellbeing_rank': response.xpath(''),
            'Access_Basic_Knowledge': response.xpath(''),
            'Access_Basic_Knowledge_rank': response.xpath(''),
            'Access_tBasic_Knowledge': response.xpath(''),
            'Information_and_Communications': response.xpath(''),
            'Information_and_Communications_rank': response.xpath(''),
            'Healthcare': response.xpath(''),
            'Healthcare_rank': response.xpath(''),
            'Environmental_quality': response.xpath(''),
            'Environmental_quality_rank': response.xpath(''),
            'Opportunity': response.xpath(''),
            'Opportunity_rank': response.xpath(''),
            'Opportunity_rank': response.xpath(''),
            'Personal_rights': response.xpath(''),
            'Personal_rights_rank': response.xpath(''),
            'Personal_Freedom_Choice': response.xpath(''),
            'Personal_Freedom_Choice_rank': response.xpath(''),
            'Inclusiveness': response.xpath(''),
            'Inclusiveness_rank': response.xpath(''),
            'Access_Advanced_Education': response.xpath(''),
            'Access_Advanced_Education_rank': response.xpath('')            
            }