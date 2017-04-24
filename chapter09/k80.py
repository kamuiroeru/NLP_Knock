# -*- coding: utf-8 -*-


def rem_waste(inlis: list) -> iter:
    """
    コーパスのリストを読んで記号を除去したイテレータを返す関数
    
    stripでコーパスの両端の記号を取り除く処理をリスト内全てのコーパスに適用(map)
    filterで空文字列を除去
    """

    return filter(lambda s: s != '', map(lambda t: t.strip('.,!?;:()[]"').strip("'"), inlis))


f = open('./enwiki-20150112-400-r10-105752.txt')

with open('out80.txt', 'w') as fo:
    for line in f:
        line = line.rstrip().split()
        fo.write(' '.join(rem_waste(line)) + '\n')

f.close()
