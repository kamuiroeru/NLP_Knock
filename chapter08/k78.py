from k76 import inputList
from k74 import likelihood
from k73 import train
from k77 import classify, ret_score
import numpy as np


if __name__ == '__main__':
    k = 5  # k分割交差検定
    border = 0.5
    s = len(inputList) // k
    splitList = [inputList[i:i + s] for i in range(0, len(inputList), s)]

    # 余ったものを最後尾に追加
    splitList[-2] = splitList[-2] + splitList[-1]
    splitList = splitList[:-1]
    print('{}分割交差検定を開始します。'.format(len(splitList)))

    rocas, precisions, recalls, F_measures = np.zeros(k * 4).reshape(4, k)  # それぞれk個の要素を持ったnp.arrayである

    for i in range(k):
        print('i = ' + str(i))
        testList = splitList[i]
        trainList = [line for l in splitList[:i] + splitList[i + 1:] for line in l]  # flatten

        wdic = train(trainList)

        paramdic = {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}
        for line in testList:
            ans, odds = likelihood(line, wdic)
            prediction = '+1' if odds > border else '-1'
            paramdic[classify('{}\t{}\t{}'.format(ans, prediction, odds))] += 1

        rocas[i], precisions[i], recalls[i], F_measures[i] \
            = ret_score(*map(lambda x: paramdic[x], ['TP', 'FP', 'TN', 'FN']))

    print('正解率:\t{}'.format(np.average(rocas)))
    print('適合率:\t{}'.format(np.average(precisions)))
    print('再現率:\t{}'.format(np.average(recalls)))
    print('F1スコア:\t{}'.format(np.average(F_measures)))
