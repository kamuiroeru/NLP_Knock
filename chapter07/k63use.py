import leveldb, pickle

db = leveldb.LevelDB('./lvdb2')

while True:
    try:
        key = input('>>>')
        if '--all' in key:
            for k, v in db.RangeIter():
                print(k.decode() + ' : ' + pickle.loadss(v))
        else:
            print(pickle.loads(db.Get(key.encode())))
    except KeyError:
        print('Error:そのKeyは存在しません')
    except KeyboardInterrupt:
        exit()
