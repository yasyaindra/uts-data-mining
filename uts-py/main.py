# Ngambil tweetnya Pak Ridwan Kamil
import configparser
import tweepy
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='ridwankamil', 
                           # 200 is the maximum allowed count
                           count=60,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )



with open('tweets.txt', 'w') as f:
    for info in tweets:
        f.write(info.full_text)
        print("\n")