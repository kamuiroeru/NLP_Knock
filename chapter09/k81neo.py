# -*- coding: utf-8 -*-

templist = []
for line in open('./useList.txt'):
    line = line.rstrip().split(' ')
    if len(line) > 1:
        templist.append(' '.join(line))

searchStr = '|'.join(templist)

from collections import defaultdict
import re

count = defaultdict(int)  # 置換した国名の種類と回数を記憶する

with open('out81.txt', 'w') as fo:
    for lc, line in enumerate(open('./out80.txt')):

        # 進行状況表示
        if lc % 10000 == 0:
            print('lc: ' + str(lc))

        for matchStr in re.findall(searchStr, line.rstrip()):
            line = line.replace(matchStr, '_'.join(matchStr.split()), 1)

        fo.write(line)  # ファイルに書き出し

import pickle

pickle.dump(count, open('k81Count.pkl', 'wb'))  # 種類と回数保存
