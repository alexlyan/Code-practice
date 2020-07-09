# libs working with twitter
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
import tweepy
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler

# working with data
import time
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import json

# Access to database
engine = create_engine('sqlite:///server_db.db', echo=True)

class TwitterClient():
    """Class for streaming twits by coordinates and radius (km). Changed None to your coordinates"""
    def __init__(self, latitude=None, longitude=None, radius=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius

    def twitter_listener(self):
        while 1:
            # Timeout 3 secs
            time.sleep(3)
            try:
                for item in tweepy.Cursor(self.twitter_client.search, result_type='recent', geocode=f'{self.latitude},'\
                                                                                            f'{self.longitude},{self.radius}km').items(3):
                    # Searching twits only in russian
                    if item._json['lang'] == 'ru':

                        # Name of user
                        user_name = item._json['user']['screen_name']
                        # Time of twitter created
                        timestamp = time.mktime(datetime.strptime(item._json['created_at'], '%a %b %d %H:%M:%S +%f %Y').timetuple())
                        # Text of twit
                        text_object = item._json['text']
                        # Hashtags of twit
                        hashtags = ', '.join(item._json['entities']['hashtags'])
                        # User Mentions of twit
                        mentions = ', '.join([x['screen_name'] for x in item._json['entities']['user_mentions']])
                        # Location of twit posted
                        location = item._json['user']['location']

                        table = pd.DataFrame(columns = ['Time_stamp', 'Username', 'Text', 'Hashtags', 'User_mentions', 'Location'], 
                                            data = [[timestamp, user_name,  text_object, hashtags, mentions, location]])

                        # Inserting values with duplicate preventing
                        table.to_sql(name='twitter_table', con=engine, if_exists = 'replace', index=False)

            except tweepy.TweepError:
                # waiting for 15 mins, then fetch last 100 twits and return to listening one twits to prevent limits
                time.sleep(60 * 15)
                for item in tweepy.Cursor(self.twitter_client.search, result_type='recent', 
                                                                        geocode=f'{self.latitude},'\
                                                                                f'{self.longitude},{self.radius}km').items(100):
                    #Searching twits only in russian
                    if item._json['lang'] == 'ru':

                        # Name of user
                        user_name = item._json['user']['screen_name']
                        # Time of twitter created
                        timestamp = time.mktime(datetime.strptime(item._json['created_at'], '%a %b %d %H:%M:%S +%f %Y').timetuple())
                        # Text of twit
                        text_object = item._json['text']
                        # Hashtags of twit
                        hashtags = ', '.join(item._json['entities']['hashtags'])
                        # User Mentions of twit
                        mentions = ', '.join([x['screen_name'] for x in item._json['entities']['user_mentions']])
                        # Location of twit posted
                        location = item._json['user']['location']

                        table = pd.DataFrame(columns = ['Time_stamp', 'Username', 'Text', 'Hashtags', 'User_mentions', 'Location'], 
                                            data = [[timestamp, user_name,  text_object, hashtags, mentions, location]])
                        
                        # Inserting values with duplicate preventing
                        table.to_sql(name='twitter_table', con=engine, if_exists = 'replace', index=False)
                continue
                
            except StopIteration:
                break

### Twitter Authenticator

class TwitterAuthenticator():
    """Twitter authentication"""
    def authenticate_twitter_app(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return auth


if __name__ == "__main__":

    Twitter_by_coords = TwitterClient()

    Twitter_by_coords.twitter_listener()
