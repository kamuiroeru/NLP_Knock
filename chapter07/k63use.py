import leveldb, pickle

db = leveldb.LevelDB('./lvdb2')

while True:
    try:
        key = input('>>>')
        if '--all' in key:
            for k, v in db.RangeIter():
                lis = pickle.loads(v)
                l = len(lis)
                print(k.decode() + ' : ' + str(lis) + ' : ' + str(l))
        else:
            lis = pickle.loads(db.Get(key.encode()))
            l = len(lis)
            print(lis, l)
    except KeyError:
        print('Error:そのKeyは存在しません')
    except KeyboardInterrupt:
        exit()
