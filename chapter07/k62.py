import leveldb

db = leveldb.LevelDB('./lvdb')

i = 0
for k, v in db.RangeIter():
    if v.decode() == 'Japan':
        i += 1

print(i)
