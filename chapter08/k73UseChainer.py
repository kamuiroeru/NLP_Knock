from chainer import Chain, optimizers, Variable, serializers
import chainer.functions as F
import chainer.links as L
import numpy as np

from k74 import inputList
from time import time

import os
os.environ["CHAINER_TYPE_CHECK"] = "0"

start = time()

numof_sentence = len(inputList)  # 入力文の数 : number of sentence
train_y = np.zeros(numof_sentence * 2, dtype=np.float32).reshape(numof_sentence, 2)  # 教師データ

hashDic = {}
for sentence, num in zip(inputList, range(numof_sentence)):
    sentence = sentence.split(' ')  # 単語ごとに区切る（先頭は +1 or -1）
    if sentence[0] == '+1':
        train_y[num][0] = 1.0
    else:
         train_y[num][1] = 1.0
    for word in sentence[1:]:
        hashDic[word] = 0

for key, idNumber in zip(hashDic, np.random.permutation(len(hashDic))):
    hashDic[key] = idNumber

numof_word = len(hashDic)

# 入力文の数 * 素性数 の 行列を作成 ( 10662 * 15415 ）
train = np.zeros(numof_sentence * numof_word, dtype=np.int32).reshape(numof_sentence, numof_word)
for sentence, num in zip(inputList, range(numof_sentence)):
    sentence = sentence.split(' ')[1:]
    for word in sentence:
        train[num][hashDic[word]] = 1

print('complete initialize : {} [sec]', format(time() - start))


class MyChain(Chain):
    def __init__(self):
        super(MyChain, self).__init__(
            l1=L.Linear(15415, 2)
        )

    def __call__(self, x):
        # return F.softmax(self.l1(x))
        return F.sigmoid(self.l1(x))

    # def fwd(self, x):

# from chainer.functions.loss.mean_squared_error import mean_squared_error

# モデル作成
model = L.Classifier(MyChain())

optimizer = optimizers.SGD()
optimizer.setup(model)

numof_epoch = 30
batchsize = 1000

for epoch in range(1, numof_epoch + 1):

    print('epoch', epoch)

    perm = np.random.permutation(numof_sentence)
    for i in range(0, numof_sentence, batchsize):
        x = Variable(train[perm[i:i + batchsize]])
        t = Variable(train_y[perm[i:i + batchsize]])

        optimizer.update(model, x, t)

serializers.save_hdf5('my.model', model)
