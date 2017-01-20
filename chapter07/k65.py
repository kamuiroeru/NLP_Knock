import pymongo

client = pymongo.MongoClient()
db = client['my']
col = db['nlp100']

query = {'name': 'Queen'}
for data in col.find(query):
    print(data)
