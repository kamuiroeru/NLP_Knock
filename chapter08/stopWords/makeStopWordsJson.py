# 同じディレクトリに存在する.txt（行区切り）や.csv（1業のみ）からStopWordリストを作り、json形式で保存する。

import json, gzip

from glob import glob


def ret_extention(fname: str) -> str:
    return fname.split('.')[-1]


if __name__ == '__main__':
    outDic = {}
    for fileName in glob('*'):
        if ret_extention(fileName) != 'py':  # scriptは除外

            if ret_extention(fileName) == 'txt':
                inList = [line.rstrip() for line in open(fileName)]
                outDic[fileName.split('.')[0]] = inList  # 拡張子抜きでキーに

            elif ret_extention(fileName) == 'csv':
                inList = [line.rstrip().split(',') for line in open(fileName)]
                map(lambda s: s.rstrip(), inList)  # リストのすべての要素に対してrstrip

            else:
                print('.' + ret_extention(fileName) + 'のファイル形式は対応していません')

    # jsonをgzipで圧縮して出力
    with gzip.open('JsonStopWordlist.json.gz', 'wb') as f:
        f.write(bytes(json.dumps(outDic), encoding='utf-8'))
