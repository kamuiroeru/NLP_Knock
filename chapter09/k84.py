import pickle
from math import log2

print('nowloading')
d = pickle.load(open('./t_c_Dic.pkl', 'rb'))
t = pickle.load(open('./t_Dic.pkl', 'rb'))
c = pickle.load(open('./c_Dic.pkl', 'rb'))
n = pickle.load(open('./n.pkl', 'rb'))


def ppmi(word: str, context: str) -> float:
    return max(log2(n * d[(word, context)] / t[word] / c[context]), 0)


if __name__ == '__main__':
    newDic = {}
    for k, v in d.items():
        if v >= 10:
            ppmis = ppmi(*k)
            if ppmis:
                newDic[k] = ppmis

    pickle.dump(newDic, open('ppmiDic.pkl', 'wb'))
