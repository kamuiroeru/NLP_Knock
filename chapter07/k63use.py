import leveldb, pickle

db = leveldb.LevelDB('./lvdb2')

while True:
    try:
        key = input('>>>')
        if '--all' in key:
            for k, v in db.RangeIter():
                for tags in pickle.loads(v):
                    print(k.decode(), 'value: ' + tags['value'] + ', count: ' + str(tags['count']))
        else:
            lis = pickle.loads(db.Get(key.encode()))
            for tags in lis:
                print(key, 'value: ' + tags['value'] + ', count: ' + str(tags['count']))
    except KeyError:
        print('Error:そのKeyは存在しません')
    except KeyboardInterrupt:
        exit()
