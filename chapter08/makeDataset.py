import numpy as np
from time import time

start = time()

from k76 import inputList
from os import chdir
import pickle

numof_sentence = len(inputList)  # 入力文の数 : number of sentence
# train_y = np.zeros(numof_sentence, dtype=np.int32).reshape(numof_sentence, 1)  # 教師データ
train_y = np.zeros(numof_sentence, dtype=np.int32)

hashDic = {}
for sentence, num in zip(inputList, range(numof_sentence)):
    sentence = sentence.split(' ')  # 単語ごとに区切る（先頭は +1 or -1）
    train_y[num] = 1 if sentence[0] == '+1' else 0
    for word in sentence[1:]:
        hashDic[word] = 0

for key, idNumber in zip(hashDic, np.random.permutation(len(hashDic))):
    hashDic[key] = idNumber

numof_word = len(hashDic)

# 入力文の数 * 素性数 の 行列を作成 ( 10662 * 15415 ）
train_x = np.zeros(numof_sentence * numof_word, dtype=np.float32).reshape(numof_sentence, numof_word)
for sentence, num in zip(inputList, range(numof_sentence)):
    sentence = sentence.split(' ')[1:]
    for word in sentence:
        train_x[num][hashDic[word]] = 1

from datetime import datetime

datestr = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

chdir('data')

np.save('train_x_' + datestr, train_x)
np.save('train_y_' + datestr, train_y)
pickle.dump({v: k for k, v in hashDic.items()}, open('hashDic.pkl', 'wb'))
# keyとvalueの入れ替え

print('complete initialize : {} [sec]'.format(time() - start))
