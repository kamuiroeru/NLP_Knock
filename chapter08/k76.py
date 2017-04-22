from k73 import *

inputList = []
for line in open('sentiment.txt'):
    lineSplit = line.rstrip().split(' ')
    inputList.append(' '.join([lineSplit[0]] + remove_waste(lineSplit[1:])))

dic = train(inputList)

# print(dic)

if __name__ == '__main__':
    border = 0.5  # 境界
    correct = 0  # 正解数
    corPos = 0
    corNeg = 0

    for sentence in inputList:
        sentList = sentence.split(' ')
        likelihood = 0.0  # 重みの合計
        for word in sentList[1:]:
            likelihood += dic[word]
        if sigmoid(likelihood) > border:
            result = '+1'
        else:
            result = '-1'

        if sentList[0] == result:
            correct += 1
            if result == '+1':
                corPos += 1
            else:
                corNeg += 1

        # デバッグ用（通過したらおかしい）
        if not 0.0 < sigmoid(likelihood) < 1:
            print('hoge')

    print('Positive正解率：{}'.format(corPos / (len(inputList) / 2)))
    print('Negative正解率：{}'.format(corNeg / (len(inputList) / 2)))
    print('合計正解率：{}'.format(correct / len(inputList)))
