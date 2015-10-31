import pprint
from twitter import *
import json
import csv

config = {}
import os
relPath =  os.path.dirname(os.path.realpath(__file__))
print relPath
execfile("config.py", config)


twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

user = ["chetan_bhagat", "SrBachchan"]

for i in user:
	print i
	results = twitter.statuses.user_timeline(screen_name = i)
	#print json.dumps(results, indent=4)
        #print json.dumps(results)
        print results[0]["text"]


def getTweets(handleName):
     return twitter.statuses.user_timeline(screen_name = handleName)	
"""

with open('chetan.csv', 'wb') as csvfile:
    data = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
   
    data.writerow(['title', 'retweet', 'faviourites'])

for i in range(10):
    
       
    data.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)))

f.close()
	

	
for status in results:
	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
	print status
	print '\n\n'
	
	"""
