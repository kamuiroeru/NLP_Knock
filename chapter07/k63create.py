import json, pickle
import leveldb

db = leveldb.LevelDB('./lvdb2')

artistDic = {}
for line in open('artist.json'):
    if '"tags"' in line.strip():
        inDic = json.loads(line)
        db.Put(inDic['name'].encode(), pickle.dumps(inDic['tags']))
        # artistDic[inDic['name']] = inDic['area']
