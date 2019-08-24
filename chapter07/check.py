import json
from pprint import pprint
from collections import defaultdict

import pymongo

# client = pymongo.MongoClient()

# my_db = 'nlp100'
# my_col = 'artists'

# db = client.nlp100
# co = db.my_artists

# artistDic = json.load(open('artist.json'))

# artistDic = {}
# for line in open('artist.json'):
#     if '"area"' in line.strip():
#         inDic = json.loads(line)
#         artistDic[inDic['name']] = inDic['area']
#         # artistDic['area'] = inDic['area']
#
import pickle, gzip
# pickle.dump(artistDic, open('name_area.kvs.pickle', 'wb'))

artistDic = pickle.load(gzip.open('name_area.kvs.pickle.gz', 'rb'))
artistDic = defaultdict(str, artistDic)

# pprint(artistDic)

while True:
    try:
        key = input('>>>')
        print(artistDic[key])
    except KeyboardInterrupt:
        exit()


# for s in open('artist.json', 'r'):
#     # print(s.rstrip())
#     # co.insert_one(json.loads(s.rstrip()))
#
# for data in co.find():
#     print(data)
# jsonDict = json.load(open('artist.json','r'))
# pprint(jsonDict)
# # print(json.dumps(, indent=4))
