import numpy as np
import pickle
from k87 import cosine
from pprint import pprint

result = np.load('result.npy')
label = pickle.load(open('label.pkl', 'rb'))

array = result[label['England']]

def cul(k, v):
    return k, cosine(array, result[v])

def procedure():
    from multiprocessing import Pool
    with Pool() as p:
        ret = p.starmap(cul, label.items())
    return ret


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        array = argv[1]

    checkDic = procedure()

    pprint(sorted(checkDic, key=lambda x: x[1], reverse=True)[1:11])
