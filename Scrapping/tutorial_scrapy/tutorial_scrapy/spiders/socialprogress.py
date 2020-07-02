import scrapy
from datetime import datetime
import time
import re
from datetime import timedelta
from scrapy_splash import SplashRequest
import pandas as pd
import numpy as np

class SocialProgress(scrapy.Spider):
    # unique name of spider
    name = 'progress'
    
    
    # # Step 1. Start scrapy
    def start_requests(self):
        self.index = 0
        
        # Load iso3 country index
        df = pd.read_csv('/Users/lyanalexandr/onedrive/projects/programming/python/practice/scrapping/tutorial_scrapy/tutorial_scrapy/spiders/iso3.csv')
        iso3_list = df['iso_alpha'].to_list()
        # main link for scrapping (all news)
        links = [f'https://www.socialprogress.org/?tab=2&code={x}' for x in iso3_list]
        for link in links:
            time.sleep(4)
            yield SplashRequest(url=link, callback=self.parse_data, args={'wait': 10})


    # Step 3. Function for extracting data from links

    def parse_data(self, response):
        
        country_name =  response.xpath('/html/body/div/main/div/div[2]/div[1]/div[1]/h2/text()').get().strip()
        country_name = country_name if country_name else np.nan
        world_position =  response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[2]/span[3]/text()').get().strip()
        world_position = world_position if world_position else np.nan
        Social_Progress_Index =  response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[2]/span[2]/text()').get().strip()
        Social_Progress_Index = Social_Progress_Index if Social_Progress_Index else np.nan
        GDP_PPP_pc =  response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/span[2]/text()').get().strip()
        GDP_PPP_pc = GDP_PPP_pc if GDP_PPP_pc else np.nan
        GDP_PPP_pc_position =  response.xpath('/html/body/div/main/div/div[2]/div[1]/div[2]/div[3]/span[3]/text()').get().strip()
        GDP_PPP_pc_position = GDP_PPP_pc_position if GDP_PPP_pc_position else np.nan
        Basic_human_needs =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/div/div[2]/span[2]/text()').get().strip()
        Basic_human_needs = Basic_human_needs if Basic_human_needs else np.nan
        Basic_human_needs_rank = response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/div/div[2]/span[3]/text()').get().strip()
        Basic_human_needs_rank = Basic_human_needs_rank if Basic_human_needs_rank else np.nan
        Basic_Medical_Care =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[1]/li[1]/span[2]/text()').get().strip()
        Basic_Medical_Care = Basic_Medical_Care if Basic_Medical_Care else np.nan
        Basic_Medical_Care_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[1]/li[1]/span[3]/text()').get().strip()
        Basic_Medical_Care_rank = Basic_Medical_Care_rank if Basic_Medical_Care_rank else np.nan
        Water_and_Sanitation =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[2]/li[1]/span[2]/text()').get().strip()
        Water_and_Sanitation = Water_and_Sanitation if Water_and_Sanitation else np.nan
        Water_and_Sanitation_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[2]/li[1]/span[3]/text()').get().strip()
        Water_and_Sanitation_rank = Water_and_Sanitation_rank if Water_and_Sanitation_rank else np.nan
        Shelter =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[3]/li[1]/span[2]/text()').get().strip()
        Shelter = Shelter if Shelter else np.nan
        Shelter_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[3]/li[1]/span[3]/text()').get().strip()
        Shelter_rank = Shelter_rank if Shelter_rank else np.nan
        Personal_safety =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[4]/li[1]/span[2]/text()').get().strip()
        Personal_safety = Personal_safety if Personal_safety else np.nan
        Personal_safety_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[1]/ul[4]/li[1]/span[3]/text()').get().strip()
        Personal_safety_rank = Personal_safety_rank if Personal_safety_rank else np.nan
        Foundations_of_Wellbeing =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/div/div[2]/span[2]/text()').get().strip()
        Foundations_of_Wellbeing = Foundations_of_Wellbeing if Foundations_of_Wellbeing else np.nan
        Foundations_of_Wellbeing_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/div/div[2]/span[3]/text()').get().strip()
        Foundations_of_Wellbeing_rank = Foundations_of_Wellbeing_rank if Foundations_of_Wellbeing_rank else np.nan
        Access_Basic_Knowledge =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[1]/li[1]/span[2]/text()').get().strip()
        Access_Basic_Knowledge = Access_Basic_Knowledge if Access_Basic_Knowledge else np.nan
        Access_Basic_Knowledge_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[1]/li[1]/span[3]/text()').get().strip()
        Access_Basic_Knowledge_rank = Access_Basic_Knowledge_rank if Access_Basic_Knowledge_rank else np.nan
        Information_and_Communications =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[2]/li[1]/span[2]/text()').get().strip()
        Information_and_Communications = Information_and_Communications if Information_and_Communications else np.nan
        Information_and_Communications_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[2]/li[1]/span[3]/text()').get().strip()
        Information_and_Communications_rank = Information_and_Communications_rank if Information_and_Communications_rank else np.nan
        Healthcare =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[3]/li[1]/span[2]/text()').get().strip()
        Healthcare = Healthcare if Healthcare else np.nan
        Healthcare_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[3]/li[1]/span[3]/text()').get().strip()
        Healthcare_rank = Healthcare_rank if Healthcare_rank else np.nan
        Environmental_quality =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[4]/li[1]/span[2]/text()').get().strip()
        Environmental_quality = Environmental_quality if Environmental_quality else np.nan
        Environmental_quality_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[2]/ul[4]/li[1]/span[3]/text()').get().strip()
        Environmental_quality_rank = Environmental_quality_rank if Environmental_quality_rank else np.nan
        Opportunity =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/div/div[2]/span[2]/text()').get().strip()
        Opportunity = Opportunity if Opportunity else np.nan
        Opportunity_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/div/div[2]/span[3]/text()').get().strip()
        Opportunity_rank = Opportunity_rank if Opportunity_rank else np.nan
        Personal_rights =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[1]/li[1]/span[2]/text()').get().strip()
        Personal_rights = Personal_rights if Personal_rights else np.nan
        Personal_rights_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[1]/li[1]/span[3]/text()').get().strip()
        Personal_rights_rank = Personal_rights_rank if Personal_rights_rank else np.nan
        Personal_Freedom_Choice = response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[2]/li[1]/span[2]/text()').get().strip()
        Personal_Freedom_Choice = Personal_Freedom_Choice if Personal_Freedom_Choice else np.nan
        Personal_Freedom_Choice_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[2]/li[1]/span[3]/text()').get().strip()
        Personal_Freedom_Choice_rank = Personal_Freedom_Choice_rank if Personal_Freedom_Choice_rank else np.nan
        Inclusiveness =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[3]/li[1]/span[2]/text()').get().strip()
        Inclusiveness = Inclusiveness if Inclusiveness else np.nan
        Inclusiveness_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[3]/li[1]/span[3]/text()').get().strip()
        Inclusiveness_rank = Inclusiveness_rank if Inclusiveness_rank else np.nan
        Access_Advanced_Education =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[4]/li[1]/span[2]/text()').get().strip()
        Access_Advanced_Education = Access_Advanced_Education if Access_Advanced_Education else np.nan
        Access_Advanced_Education_rank =  response.xpath('/html/body/div/main/div/div[3]/div/detail/div/div[1]/div[3]/ul[4]/li[1]/span[3]/text()').get().strip()
        Access_Advanced_Education_rank = Access_Advanced_Education_rank if Access_Advanced_Education_rank else np.nan

        yield {        
            'country_name': country_name,
            'world_position': world_position,
            'Social_Progress_Index': Social_Progress_Index,
            'GDP_PPP_pc': GDP_PPP_pc,
            'GDP_PPP_pc_position': GDP_PPP_pc_position,
            'Basic_human_needs': Basic_human_needs,
            'Basic_human_needs_rank':Basic_human_needs_rank,
            'Basic_Medical_Care': Basic_Medical_Care,
            'Basic_Medical_Care_rank:': Basic_Medical_Care_rank,
            'Water_and_Sanitation': Water_and_Sanitation,
            'Water_and_Sanitation_rank': Water_and_Sanitation_rank,
            'Shelter': Shelter,
            'Shelter_rank': Shelter_rank,
            'Personal_safety': Personal_safety,
            'Personal_safety_rank': Personal_safety_rank,
            'Foundations_of_Wellbeing': Foundations_of_Wellbeing,
            'Foundations_of_Wellbeing_rank': Foundations_of_Wellbeing_rank,
            'Access_Basic_Knowledge': Access_Basic_Knowledge,
            'Access_Basic_Knowledge_rank': Access_Basic_Knowledge_rank,
            'Information_and_Communications': Information_and_Communications,
            'Information_and_Communications_rank': Information_and_Communications_rank,
            'Healthcare': Healthcare,
            'Healthcare_rank': Healthcare_rank,
            'Environmental_quality': Environmental_quality,
            'Environmental_quality_rank': Environmental_quality_rank,
            'Opportunity': Opportunity,
            'Opportunity_rank': Opportunity_rank,
            'Personal_rights': Personal_rights,
            'Personal_rights_rank': Personal_rights_rank,
            'Personal_Freedom_Choice': Personal_Freedom_Choice,
            'Personal_Freedom_Choice_rank': Personal_Freedom_Choice_rank,
            'Inclusiveness': Inclusiveness,
            'Inclusiveness_rank': Inclusiveness_rank,
            'Access_Advanced_Education': Access_Advanced_Education,
            'Access_Advanced_Education_rank': Access_Advanced_Education_rank
            }

            