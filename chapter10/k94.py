from k90gensim import model
from sys import path
path.append('../chapter09')
import k88modNonzero as k88
from k87 import cosine
import numpy as np

import pandas as pd

df = pd.read_csv('./wordsim353/combined.csv')
print(df)

cosGensims = [cosine(model[d['Word 1']], model[d['Word 2']]) for lc, d in df.iterrows()]

def retArray(instr):
    try:
        return k88.decompMat[k88.label[instr]]
    except KeyError:
        return np.zeros(300)


cosMysystems = [cosine(retArray(d['Word 1']),
                       retArray(d['Word 2'])) for lc, d in df.iterrows()]

df['gensim'] = list(map(lambda x: '{:0.2f}'.format(x * 10), cosGensims))
df['mysystem'] = list(map(lambda x: '{:0.2f}'.format(x * 10), cosMysystems))

print(df)

df.to_csv('out94.csv')
