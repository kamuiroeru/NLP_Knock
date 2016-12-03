import gzip
import pickle


def pickleDump(obj=[], filename='', comp=False, level=1):
    pickle_str = pickle.dumps(obj)

    if comp or '.gz' in filename:  # 圧縮指定された時
        filename = filename.rsplit('.', 1)[0]
        gzip.open(filename + '.gz', 'wb').write(gzip.compress(pickle_str, compresslevel=level))
        return

    filename = filename.rsplit('.', 1)[0]
    with open(filename + '.pickle', 'wb') as f:
        f.write(pickle_str)


def pickleLoad(filename=''):
    if '.gz' not in filename or '.pickle' not in filename:
        print('対応していないファイルです。')

    if '.gz' in filename:  # 圧縮されてた時
        with gzip.open(filename) as f:
            return pickle.loads(f.read())

    else:
        with open(filename, 'rb') as f:
            return pickle.load(f)
