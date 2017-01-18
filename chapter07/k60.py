import leveldb
import json

db = leveldb.LevelDB()

artistDic = {}
for line in open('artist.json'):
    if '"area"' in line.strip():
        inDic = json.loads(line)
        db.Put(inDic['name'], inDic['area'])
        artistDic[inDic['name']] = inDic['area']
