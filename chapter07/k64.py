import pymongo

client = pymongo.MongoClient()
db = client.test
co = db.myCol

co.delete_one({"test":3})

for data in co.find():
    print(data)