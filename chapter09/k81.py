# -*- coding: utf-8 -*-

firstSet = set()
secondSet = set()

for line in open('./useList.txt'):
    line = line.rstrip().split(' ')
    if len(line) > 1:
        firstSet.add(line[0])
        secondSet.add(' '.join(line))

f = open('./out80.txt')

from collections import defaultdict

count = defaultdict(int)

with open('out81.txt', 'w') as fo:
    for lc, line in enumerate(f):
        print('lc: ' + str(lc))
        tokens = line.rstrip().split()
        outlist = []
        i = 0
        while len(tokens) > i:
            if tokens[i] in firstSet:
                isCountryName = False
                j = 1
                while not isCountryName and j <= 5:
                    isCountryName = ' '.join(tokens[i:i + j]) in secondSet
                    j += 1
                if isCountryName:
                    specialToken = '_'.join(tokens[i:i + j - 1])
                    count[specialToken] += 1
                    outlist.append(specialToken)
                    i += j - 1
                    continue
            outlist.append(tokens[i])
            i += 1
        fo.write(' '.join(outlist) + str('\n'))

import pickle

pickle.dump(count, open('k81Count.pkl', 'wb'))
