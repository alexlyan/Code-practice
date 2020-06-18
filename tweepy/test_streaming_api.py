from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from lucid_tweepy import twitter_credentials
import json
import pandas as pd

class TwitterSteamer():
    def __init__(self):
        pass

    def stream_tweets(self, hash_tag_list):
        

        # Twitter Authentication and connection to Twitter
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)

#### Stream Listener
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self):
        # self.file_name = file_name
        pass
    def on_data(self, data):
        # try:
        data = {"text": [str(json.loads(data)['text'])],
                "created at":[json.loads(data)['created_at']]}
        print(data)
        # print(str(json.loads(data)['text']))
        df = pd.DataFrame(data)

        #delete after creating table
        # df.to_csv('table.csv')

        with open('table.csv', 'a') as tf:
            df.to_csv(tf, header=False)
          

    def on_error(self, status):
        if status == '420':
            return False
        print(status)

# def stream_hashtags(n):
#     # Authenticate using config.py and connect to Twitter Streaming API.
#     twitter_streamer = TwitterSteamer()
#     twitter_streamer.stream_tweets(n)
if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    twitter_streamer = TwitterSteamer()
    twitter_streamer.stream_tweets(['kyrgyzstan'])

        


     
    
