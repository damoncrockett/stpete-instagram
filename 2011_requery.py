import pymongo
import pandas as pd
import numpy as np
from bson.objectid import ObjectId

client = pymongo.MongoClient()
db = client.sample_tweets
coll = db.sample_tweets_collection

query = {'geo' : {"$exists" : 1}}
projection = {'geo.coordinates': 1, '_id' : 1}
cur = coll.find(query,projection)

metadata = [m for m in cur]
mongo_id = [item['_id'] for item in metadata]

lat = [item['geo']['coordinates'][0] for item in metadata]
lon = [item['geo']['coordinates'][1] for item in metadata]

df = pd.DataFrame(mongo_id,columns=['mongo_id'])
df['lat'] = lat
df['lon'] = lon

df.to_csv("/data/damoncrockett/twitter_metadata_2011.csv", index=False)