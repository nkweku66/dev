import tweepy
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('CONSUMER_KEY')
access_token_secret = os.getenv('CONSUMER_KEY_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')


# auth = tweepy.OAuth2AppHandler(access_token, access_token_secret)
client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret, 
    access_token=access_token, 
    access_token_secret=access_token_secret
)

client.create_tweet(text="Hello X")


# print(f"This is {user}")
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

