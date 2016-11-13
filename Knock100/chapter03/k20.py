import json
import gzip


def read_jwc_json(filename='jawiki-country.json.gz'):
    dic_jwc = {}
    with gzip.open(filename, 'r') as f:
        for line in f:
            obj = json.loads(line.decode('utf-8'))
            dic_jwc[obj['title']] = obj['text']
    return dic_jwc


if __name__ == '__main__':
    print(read_jwc_json()['イギリス'])
