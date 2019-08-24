import pymongo

col = pymongo.MongoClient()['my']['nlp100']

hoge = set()
for data in col.find():
    if data.get('tags'):
        if data.get('tags')[0].get('value'):
            hoge.add(data.get('tags')[0].get('value'))
    # huga.append(data.get('tags.value'))
print(hoge)
