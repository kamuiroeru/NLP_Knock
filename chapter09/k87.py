import numpy as np
import pickle
from sys import argv

def cosine(x, y):
    """2つのnumpy配列からCosine類似度を返す"""

    normX = np.linalg.norm(x)
    normY = np.linalg.norm(y)
    return x.dot(y) / normX / normY


if __name__ == '__main__':
    str1 = 'United_States'
    str2 = 'U.S'

    if len(argv) == 3:
        str1 = argv[1]
        str2 = argv[2]

    result = np.load('result.npz')
    label = pickle.load(open('label.pkl', 'rb'))

    x = result[label[str1]]
    y = result[label[str2]]
    print('「{}」と「{}」のcosine類似度は{:0.2f}'
          .format(str1, str2, cosine(x, y)))
