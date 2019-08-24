import pickle
from math import log2
from multiprocessing import Pool

print('nowloading')
d = pickle.load(open('./t_c_Dic.pkl', 'rb'))
t = pickle.load(open('./t_Dic.pkl', 'rb'))
c = pickle.load(open('./c_Dic.pkl', 'rb'))
n = pickle.load(open('./n.pkl', 'rb'))
print('done')

print('StartCulculate')
def ppmi(word: str, context: str) -> float:
    return max(log2(n * d[(word, context)] / t[word] / c[context]), 0)

def culculate(k, v):
    if v >= 10:
        ppmis = ppmi(*k)
        if ppmis:
            return k, ppmis  # kはタプル


if __name__ == '__main__':
    with Pool() as p:
        retVal = p.starmap(culculate, d.items())

    newDic = {elem[0]: elem[1] for elem in retVal if elem}

    pickle.dump(newDic, open('ppmiDic2.pkl', 'wb'))
