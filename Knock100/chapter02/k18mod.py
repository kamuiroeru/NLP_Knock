# 動きません

import re

newList = []
with open('hightemp.txt', 'r') as f:
    newList = [f.readlines()[key] for key, value in sorted({i: re.split('[ \t]+', line)[2] for i, line in zip(range(len(f.readlines())), f.readlines())}.items(), key=lambda x:x[1])]

for l in newList:
    print(l)
