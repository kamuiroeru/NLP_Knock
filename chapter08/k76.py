from k72 import remove_waste
from k74 import likelihood

inputList = []
for line in open('sentiment.txt'):
    lineSplit = line.rstrip().split(' ')
    inputList.append(' '.join([lineSplit[0]] + remove_waste(lineSplit[1:])))


if __name__ == '__main__':
    border = 0.5  # 境界

    for sentence in inputList:
        ans, odds = likelihood(sentence)
        print(*(ans, '+1' if odds > border else '-1', odds), sep='\t')
