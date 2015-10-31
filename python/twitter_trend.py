import json
from twitter import *


config = {}
execfile("config.py", config)


twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))



results = twitter.trends.place(_id = 23424848)


print json.dumps(results, indent=4)


"""for location in results:
	for trend in location["trends"]:
		print " - %s" % trend["name"]
"""