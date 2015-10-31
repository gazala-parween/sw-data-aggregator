import tweepy
import json
from datetime import datetime


consumer_key = 'Mqn1gEwkThO7puYnXQW8wJzEv'
consumer_secret = 'p27JR9z378Ma9qbdhoRfPnI5ISnQUtFepMirzXhFGPyI9JuTHV'
access_token =  '3944171172-oGJ8S6DmDnqMc2uNwRtreVyxdTXFRQZcFVsENjY'
access_token_secret =  'r9w7P4Ht0NQcHHL6Ni3PJv3EpOi2VbAsQcaDeVuagR0td'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users = api.user_timeline(screen_name = 'chetan_bhagat')

print users



"""for user  in users[0]:
	print user['_json']









f = open("twitter_latest.csv","wb+")
cs = csv.writer(f)
cs.writerow(["text","favorite_count","retweet_coun","location","name","promoted_content"])

    for idxx, trend in enumerate(data):    
        cs.writerow([(idxx+1),trend["url"].replace('%23','#').replace('%22','"').encode('utf-8'),trend["query"].replace('%23','#').replace('%22','"').encode('utf-8'),placesN[idx],trend["name"].encode('utf-8'),trend["promoted_content"]])


for idx,place in enumerate(places):
    getTrend = api.trends_place(place)
    data = getTrend[0]["trends"]
    for idxx, trend in enumerate(data):    
        print (idxx+1),trend["url"].replace('%23','#').replace('%22','"').encode('utf-8'),trend["query"].replace('%23','#').replace('%22','"').encode('utf-8'),placesN[idx],trend["name"].encode('utf-8'),trend["promoted_content"]


getTrend = api.trends_place(23424848)
data = getTrend[0]
print json.dumps(data)

"""
