import pickle
from scipy.sparse import lil_matrix, csr_matrix, linalg
import numpy as np
from sklearn.decomposition import TruncatedSVD, PCA
from scipy import io
from time import time

start = time()
print('Loading, Pickling')
label = {v: lc for lc, v in enumerate(pickle.load(open('./t_Dic.pkl', 'rb')))}
pickle.dump(label, open('label.pkl', 'wb'))

# print(labelC['United_States'])
matrix = lil_matrix((len(label), len(label)))

for k, v in pickle.load(open('./ppmiDic.pkl', 'rb')).items():
    matrix[label[k[0]], label[k[1]]] = v
print('Done {} [sec]'.format(time() - start))

print('元の行列:{} × {}'.format(*matrix.shape))

start = time()
print('decompressing and fitting')
decomp = TruncatedSVD(300)
decomp.fit(matrix)
print('Done {} [sec]'.format(time() - start))

start = time()
print('transforming')
decompMatrix = decomp.transform(matrix)
print('Done {} [sec]'.format(time() - start))

start = time()
print('doing PCA')
pca = PCA(300)
result = pca.fit_transform(decompMatrix)
print('Done {} [sec]'.format(time() - start))

print('圧縮後の行列:{} × {}'.format(*result.shape))

start = time()
print('savingResult')
np.savez('result', result)
print('Done {} [sec]'.format(time() - start))
