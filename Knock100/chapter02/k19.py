import re
from collections import defaultdict

dic = defaultdict(list)
lines = []
with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

for i, line in zip(range(len(lines)), lines):
    lSplited = re.split(r'[ \t]+', line)
    if not dic[lSplited[0]]:  # 新しいタイプ（空リスト）だったら、要素を追加 if dic[(ry)] == [] と同じ
        dic[lSplited[0]].append(1)
    else:
        dic[lSplited[0]][0] += 1
    dic[lSplited[0]].append(i)

# newList = []
# for key, value in sorted(dic.items(), key=lambda x: x[1][0], reverse=True):
#     for index in value:
#         newList.append(lines[index])
newList = [lines[index] for key, value in sorted(dic.items(), key=lambda x: x[1][0], reverse=True) for index in value[1:]]

for l in newList:
    print(l, end='')
