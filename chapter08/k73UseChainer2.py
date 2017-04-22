from chainer import Chain, optimizers, Variable, serializers, iterators, training
import chainer.functions as F
import chainer.links as L
import numpy as np
from chainer.training import extensions
from chainer.datasets.tuple_dataset import TupleDataset
from chainer.functions.loss.mean_squared_error import mean_squared_error

from time import time
start = time()

from k74 import inputList

# import os
#
# os.environ["CHAINER_TYPE_CHECK"] = "0"


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

# train = np.hstack((train_x, train_y))
train = TupleDataset(train_x, train_y)

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


batchsize = 1000
numof_epoch = 100

train_iter = iterators.SerialIterator(train, batchsize)
test_iter = iterators.SerialIterator(train, batchsize, repeat=False, shuffle=False)

from chainer.functions.loss.mean_squared_error import mean_squared_error

# モデル作成
model = L.Classifier(MyChain(), lossfun=mean_squared_error)
# model = L.Classifier(MyChain())

optimizer = optimizers.SGD()
optimizer.setup(model)

updater = training.StandardUpdater(train_iter, optimizer)
trainer = training.Trainer(updater, (numof_epoch, 'epoch'))

trainer.extend(extensions.Evaluator(test_iter, model))
# これはいる。test_iterを使ってepochごとに評価してる（と思う）
trainer.extend(extensions.dump_graph('main/loss'))
# ネットワークの形をグラフで表示できるようにdot形式で保存する。
# trainer.extend(extensions.snapshot(), trigger=(numof_epoch, 'epoch'))
# epochごとのtrainerの情報を保存する。それを読み込んで、途中から再開などができる。これけすと結構早くなったりした？
trainer.extend(extensions.LogReport())
# epochごとにlogをだす
trainer.extend(extensions.PrintReport(
    ['epoch', 'main/loss', 'validation/main/loss',
     'main/accuracy', 'validation/main/accuracy']))
# logで出す情報を指定する。
trainer.extend(extensions.ProgressBar())
# 今全体と、epochごとでどのぐらい進んでいるかを教えてくれる。

trainer.run()
# trainerをいろいろ設定した後、これをやって実際に実行する。これは必須

#
# for epoch in range(1, numof_epoch + 1):
#
#     print('epoch', epoch)
#
#     perm = np.random.permutation(numof_sentence)
#     for i in range(0, numof_sentence, batchsize):
#         x = Variable(train[perm[i:i + batchsize]])
#         t = Variable(train_y[perm[i:i + batchsize]])
#
#         optimizer.update(model, x, t)
#
# serializers.save_hdf5('my.model', model)
