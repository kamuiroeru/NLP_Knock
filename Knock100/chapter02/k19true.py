import re
from collections import defaultdict
from sys import argv


lines = []
with open(argv[1], 'r') as f:
    lines = f.readlines()

dic = defaultdict(list)
for i, token in enumerate([re.split('[ \t]+', line)[0] for line in lines]):
    dic[token].append(i)

# newList = []
# for key, value in sorted(dic.items(), key=lambda x: len(x[1]), reverse=True):
#     for index in value:
#         newList.append(lines[index])
newList = [lines[index] for key, value in sorted(dic.items(), key=lambda x: len(x[1]), reverse=True) for index in value]

for l in newList:
    print(l, end='')
