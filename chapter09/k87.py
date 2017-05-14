import numpy as np
import pickle


def cosine(x, y):
    """2つのnumpy配列からCosine類似度を返す"""

    normX = np.linalg.norm(x)
    normY = np.linalg.norm(y)
    return x.dot(y) / normX / normY


result = np.load('result.npz')
label = pickle.load(open('label.pkl', 'rb'))

x = result[label['United_States']]
y = result[label['U.S']]
print(cosine(x, y))
