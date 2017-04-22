from k72 import remove_waste
from k74 import likelihood

inputList = []
for line in open('sentiment.txt'):
    lineSplit = line.rstrip().split(' ')
    inputList.append(' '.join([lineSplit[0]] + remove_waste(lineSplit[1:])))


if __name__ == '__main__':
    border = 0.5  # 境界

    for sentence in inputList:
        res, odds = likelihood(sentence)
        print('{}\t{}\t{}'.format(res, '+1' if odds > border else '-1', odds))
