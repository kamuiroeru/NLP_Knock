import leveldb
import json

db = leveldb.LevelDB('./lvdb')

artistDic = {}
for line in open('artist.json'):
    if '"area"' in line.strip():
        inDic = json.loads(line)
        db.Put(inDic['name'].encode(), inDic['area'].encode())
        # artistDic[inDic['name']] = inDic['area']
