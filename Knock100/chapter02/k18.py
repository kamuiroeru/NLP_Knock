import re

lines = []
with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

# dic = {}
# for i, line in zip(range(len(lines)), lines):
#     dic[i] = re.split(r'[ \t]+', line)[2]
dic = {i: re.split('[ \t]+', line)[2] for i, line in zip(range(len(lines)), lines)}

# newList = []
# for key, value in sorted(dic.items(), key=lambda x: x[0]):
#     newList.append(lines[key])
newList = [lines[key] for key, value in sorted(dic.items(), key=lambda x:x[1], reverse=True)]

for l in newList:
    print(l, end='')
