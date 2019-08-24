from chainer import Chain, optimizers, Variable, serializers, iterators, training
import chainer.functions as F
import chainer.links as L
import numpy as np
from chainer.training import extensions
from chainer.datasets.tuple_dataset import TupleDataset
from chainer.functions.loss.mean_squared_error import mean_squared_error

# train = np.hstack((train_x, train_y))
train = TupleDataset(np.load('data/train_x_2017_05_07__19_39_15.npy'), np.load('data/train_y_2017_05_07__19_39_15.npy'))


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
numof_epoch = 10

train_iter = iterators.SerialIterator(train, batchsize)
test_iter = iterators.SerialIterator(train, batchsize, repeat=False, shuffle=False)

from chainer.functions.loss.mean_squared_error import mean_squared_error

# モデル作成
# model = L.Classifier(MyChain(), lossfun=mean_squared_error)
model = L.Classifier(MyChain())

# optimizer = optimizers.SGD()
optimizer = optimizers.Adam()
optimizer.setup(model)

updater = training.StandardUpdater(train_iter, optimizer)

from datetime import datetime

datestr = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")

trainer = training.Trainer(updater, (numof_epoch, 'epoch'), out='result/' + datestr)

import pickle

hashDic = pickle.load(open('./data/hashDic.pkl', 'rb'))


@training.make_extension(trigger=(5, 'epoch'), default_name='predict')
def predict(trainer):
    wrongs = [('x', 'y', 'ans')]
    for x, ans in train:
        y = model.predictor(x.reshape(1, 15415))
        y = F.sigmoid(y).data.argmax()
        if y != ans:
            wrongs.append((x, y, ans))
    pickle.dump(wrongs, open(trainer.out + '/wrongs_{}.pkl'.format(trainer.updater.epoch), 'wb'))

trainer.extend(extensions.Evaluator(test_iter, model))
# これはいる。test_iterを使ってepochごとに評価してる（と思う）
# trainer.extend(extensions.dump_graph('main/loss'))
# ネットワークの形をグラフで表示できるようにdot形式で保存する。
# trainer.extend(extensions.snapshot(), trigger=(5, 'epoch'))
# epochごとのtrainerの情報を保存する。それを読み込んで、途中から再開などができる。これけすと結構早くなったりした？
trainer.extend(extensions.LogReport(trigger=(1, 'epoch')))
# epochごとにlogをだす
trainer.extend(extensions.PrintReport(
    ['epoch', 'main/loss', 'validation/main/loss',
     'main/accuracy', 'validation/main/accuracy']))

# logで出す情報を指定する。

import matplotlib

trainer.extend(extensions.PlotReport(['main/accuracy', 'main/loss', 'validation/main/loss',
                                      'main/accuracy', 'validation/main/accuracy']))

trainer.extend(extensions.ProgressBar())
# 今全体と、epochごとでどのぐらい進んでいるかを教えてくれる。

trainer.extend(predict)

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
