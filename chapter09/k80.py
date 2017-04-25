# -*- coding: utf-8 -*-


def rem_waste(inlis: list) -> iter:
    """
    コーパスのリストを読んで記号を除去したイテレータを返す関数
    
    stripでコーパスの両端の記号を取り除く処理をリスト内全てのコーパスに適用(map)
    filterで空文字列を除去
    """

    return filter(lambda s: s != '', map(lambda t: t.strip('`.,!?;:()[]\'"“”‘’：；‘,'), inlis))


f = open('./enwiki-20150112-400-r10-105752.txt')

with open('out80.txt', 'w') as fo:
    for lc, line in enumerate(f):
        if lc % 1000 == 0:
            print('lc: ' + str(lc))
        line = line.rstrip().split()
        fo.write(' '.join(rem_waste(line)) + '\n')

        # デバッグ用
        # if lc > 200:
        #     break
f.close()
