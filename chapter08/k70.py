posList = []
for line in open('rt-polaritydata/rt-polarity.pos', 'rb'):
    posList.append('+1 ' + line.decode(encoding='latin'))

negList = []
for line in open('rt-polaritydata/rt-polarity.neg', 'rb'):
    negList.append('-1 ' + line.decode(encoding='latin'))

print(len(posList), len(negList))

from random import shuffle
outList = posList + negList
shuffle(outList)

with open('sentiment.txt', 'w') as f:
    for line in outList:
        f.write(line)
