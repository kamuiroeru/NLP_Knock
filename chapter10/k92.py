from k90gensim import model
from sys import path
path.append('../chapter09')
import k88modNonzero as k88
import numpy as np

def bestAns(pos: list, neg: list):
    arr = np.zeros(300)
    for p in pos:
        try:
            arr += k88.decompMat[k88.label[p]]
        except KeyError:
            pass
    for n in neg:
        try:
            arr -= k88.decompMat[k88.label[p]]
        except KeyError:
            pass

    k88.array = arr
    return sorted(k88.procedure(), key=lambda x: x[1], reverse=True)[1]

def crop(infloat):
    return '{:0.3f}'.format(infloat)


with open('./out92.txt', 'w') as f:
    for line in open('./out91.txt'):
        col = line.rstrip().split(' ')
        pos, neg = [col[2], col[1]], [col[0]]  # 振り分け
        out = model.most_similar(topn=1, positive=pos, negative=neg)
        out88 = bestAns(pos, neg)
        # print(out88)
        outstr = col + [out[0][0], crop(out[0][1]), out88[0], crop(out88[1])]
        print(outstr)  # 結果確認
        f.write(' '.join(outstr) + '\n')  # 書き込み
