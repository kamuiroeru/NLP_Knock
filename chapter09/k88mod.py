import numpy as np
import pickle
from k87 import cosine

decompMat = np.load('../chapter09/decompMat.npy')
label = pickle.load(open('../chapter09/label.pkl', 'rb'))

array = decompMat[label['England']]

def cul(k, v):
    return k, cosine(array, decompMat[v])

def procedure():
    from multiprocessing import Pool
    with Pool() as p:
        ret = p.starmap(cul, label.items())
    return ret


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        array = decompMat[label[argv[1]]]

    checkDic = procedure()

    best10 = sorted(checkDic, key=lambda x: x[1], reverse=True)[1:11]

    for word, cos in best10:
        print('{}\t\t{:0.2f}'.format(word, cos))
