# -*- coding: utf-8 -*-

firstSet = set()  # 2つ以上の単語からなる国名のうち、先頭の単語のみを保持
secondSet = set()  # 2つ以上の単語からなる国名全ての単語を保持

# 国名リストを読み込んで、2つの集合を作成
for line in open('./useList.txt'):
    line = line.rstrip().split(' ')
    if len(line) > 1:
        firstSet.add(line[0])
        secondSet.add(' '.join(line))

f = open('./out80.txt')

from collections import defaultdict

count = defaultdict(int)  # 置換した国名の種類と回数を記憶する

with open('out81.txt', 'w') as fo:
    for lc, line in enumerate(f):

        # 進行状況表示
        if lc % 1000 == 0:
            print('lc: ' + str(lc))

        tokens = line.rstrip().split()
        outlist = []
        i = 0
        while len(tokens) > i:
            if tokens[i] in firstSet:  # 国名の先頭の単語になりそうな単語を見つけたら
                isCountryName = False
                j = 1
                while not isCountryName and j <= 5:  # 5回まで単語を繋げて検索
                    isCountryName = ' '.join(tokens[i:i + j]) in secondSet
                    j += 1
                if isCountryName:  # 国名が見つかったら
                    specialToken = '_'.join(tokens[i:i + j - 1])  # _で結合して文字列に
                    count[specialToken] += 1  # 種類と回数を記録
                    outlist.append(specialToken)  # 出力用リストに記録
                    i += j - 1  # ラベルの帳尻合わせ
                    continue

            # 国名じゃなかった単語はそのまま追加
            outlist.append(tokens[i])
            i += 1
        fo.write(' '.join(outlist) + str('\n'))  # ファイルに書き出し

import pickle

pickle.dump(count, open('k81Count.pkl', 'wb'))  # 種類と回数保存
