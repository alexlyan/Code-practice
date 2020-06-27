from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json


### TWITTER CLIENT
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets
    
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


### Twitter Authenticator

class TwitterAuthenticator():
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():
    """
    Class for streaming and processing Live tweets
    """
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
    # This handles twitter authentication and the connection to the Twitter Streaming API

        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords
        stream.filter(track=hash_tag_list)

class TwitterListener(StreamListener):
    """
    This a basic listener class that just prints received to stdout
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)

            return True
        
        except BaseException as e:
            print('Error on data: %s' % str(e))
        return True
        
    def on_error(self, status):
        if status == 420:
            # Return False on_data method in case rate limit occurs.
            return False
        print(status)

if __name__ == '__main__':
    hash_tag_list = []
    fetched_tweets_filename = "tweets.txt"

    # fetching user info
    twitter_client = TwitterClient('pycon')
    # select pycon twitter user and its first 5 posts
    for tweet in twitter_client.get_user_timeline_tweets(5):
        # print(tweet)
        jsn = tweet._json
        print(jsn)
    
    # uncomment for using twitter streamer

    # twitter_streamer = TwitterStreamer()
    # twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

