import tweepy

with open("secrets.txt", "r") as s:
    secrets = s.readlines()
    consumer_key = secrets[1][:-1]
    consumer_secret = secrets[3][:-1]
    access_token = secrets[5][:-1]
    access_token_secret = secrets[7][:-1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_30_day("dev30", "@LCWaikiki")
with open("tweets.txt", "w") as f:
    for tweet in public_tweets:
        f.write(tweet.text + "\n============\n")
