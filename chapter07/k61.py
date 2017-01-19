import leveldb

db = leveldb.LevelDB('./lvdb')

while True:
    try:
        key = input('>>>')
        if '--all' in key:
            for k, v in db.RangeIter():
                print(k.decode() + ' : ' + v.decode())
        else:
            print(db.Get(key.encode()).decode())
    except KeyError:
        print('Error:そのKeyは存在しません')
    except KeyboardInterrupt:
        exit()
