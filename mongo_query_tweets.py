import pymongo
import pandas as pd
import numpy as np
from bson.objectid import ObjectId
import sys

year = sys.argv[1]

client = pymongo.MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

DIR = "/data/damoncrockett/stpete/tweets/"

tmp = pd.read_csv(DIR+str(year)+".csv")
ids = list(tmp.mongo_id)
ids = [ObjectId(item) for item in ids]

query = {'_id': {'$in': ids},
         'geo' : {"$exists" : 1}, 
         'twitter_entities.media.media_url' : {"$exists" : 1}
         }
         
projection = {'_id' : 1, 
              'body' : 1,
              'twitter_entities.media.media_url': 1,
              'geo.coordinates': 1,
              'postedTime': 1,
              'actor.id': 1
              }

cur = coll.find(query,projection)

metadata = [m for m in cur]

mongo_id = [item['_id'] for item in metadata]
text = [item['body'] for item in metadata]
text = [item.encode('utf-8') if isinstance(item,unicode) else item for item in text]
lat = [item['geo']['coordinates'][0] for item in metadata]
lon = [item['geo']['coordinates'][1] for item in metadata]
dl_url = [item['twitter_entities']['media'][0]['media_url'] for item in metadata]
postedTime = [item['postedTime'] for item in metadata]
actor_id = [item['actor']['id'] for item in metadata]

df = pd.DataFrame(mongo_id,columns=['mongo_id'])
df['text'] = text
df['lat'] = lat
df['lon'] = lon
df['dl_url'] = dl_url
df['postedTime'] = postedTime
df['actor_id'] = actor_id

df.to_csv(DIR + str(year) + "_rich.csv", index=False)