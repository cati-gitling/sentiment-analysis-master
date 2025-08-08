#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "ggtJc9lNBNliZXML2bNYIZptZ"
consumer_secret = "U1XTAClYXc133e9lvEM8jHPa9TRIGb5UbN9h3zUHSLaKGlugHn"
access_key = "4408689029-xTzjHraxDldXsXuvBQTbMXawxK1ApuwEPFuSg3J"
access_secret = "rId4v4MsKwFT7kZLgBZg9028vdfzsOz8MQ2wtQovXaRBJ"

#method to get a user's last tweets
def get_tweets(realDonaldTrump):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want
	number_of_tweets = 3200

	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = realDonaldTrump, tweet_mode = "extended", include_rts = False).items(number_of_tweets):
        #create array of tweet information: realDonaldTrump, tweet id, date/time, text
		tweets_for_csv.append([realDonaldTrump, tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")])

	#write to a new csv file from the array of tweets
	outfile = realDonaldTrump + "_tweets.csv"
	print("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print("Error: enter one username") 

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
