import gzip
import pickle
import re


def pickleDump(obj=None, filename='', comp=False, level=1):
    if obj is None:
        obj = {'hoge': 'hoge'}
    pickle_str = pickle.dumps(obj)

    if comp or '.gz' in filename:  # 圧縮指定された時
        filename = filename.rsplit('.', 1)[0]
        gzip.open(filename + '.gz', 'wb', compresslevel=level).write(pickle_str)
        return

    filename = filename.rsplit('.', 1)[0]
    with open(filename + '.pickle', 'wb') as f:
        f.write(pickle_str)


def pickleLoad(filename=''):
    if not re.findall("\.gz|\.pickle", filename):
        print('対応していないファイルです。')

    if '.gz' in filename:  # 圧縮されてた時
        with gzip.open(filename, 'rb') as f:
            return pickle.loads(f.read())

    else:
        with open(filename, 'rb') as f:
            return pickle.load(f)
