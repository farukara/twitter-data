import tweepy
from os import path

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

count = 0
if path.isfile("tweets.txt"):
    print("file already exist")
    with open("tweets.txt", "r") as f:
        old_data = f.read()
    old_data = old_data.split("\n============\n")
    with open("tweets.txt", "a") as f:
        for tweet in public_tweets:
            if tweet.text in old_data:
                print("tweet already exist in the file")
                print(tweet.text)
                continue
            else:
                count +=1
                f.write(tweet.text + "\n============\n")
else:
    print("file does not exist")
    with open("tweets.txt", "w") as f:
        for tweet in public_tweets:
            count +=1
            f.write(tweet.text + "\n============\n")

print(count, "number of tweets added to file")
