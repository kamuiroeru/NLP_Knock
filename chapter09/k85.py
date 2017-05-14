import pickle
from scipy.sparse import lil_matrix, csr_matrix, linalg
import numpy as np


def save_sparse_csr(filename, array):
    np.savez(filename, data=array.data, indices=array.indices,
             indptr=array.indptr, shape=array.shape)


def load_sparse_csr(filename):
    loader = np.load(filename)
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),
                      shape=loader['shape'])


if __name__ == '__main__':
    labelT = {v: lc for lc, v in enumerate(pickle.load(open('./t_Dic.pkl', 'rb')))}
    labelC = {v: lc for lc, v in enumerate(pickle.load(open('./c_Dic.pkl', 'rb')))}

    pickle.dump(labelC, open('labelC.pkl', 'wb'))
    pickle.dump(labelT, open('labelT.pkl', 'wb'))

    # print(labelC['United_States'])
    matrix = lil_matrix((len(labelT), len(labelC)))

    for k, v in pickle.load(open('./ppmiDic.pkl', 'rb')).items():
        matrix[labelT[k[0]], labelC[k[1]]] = v

    matrix = matrix.tocsr()

    print('元の行列:{} × {}'.format(*matrix.shape))

    E, V = linalg.eigs(matrix, k=300)

    # compressed = matrix.dot(V)
    compressed = matrix.dot(lil_matrix(V).tocsr())

    print('圧縮後の行列:{} × {}'.format(*compressed.shape))

    # pickle.dump(compressed, open('compressedMatrix.pkl', 'wb'))
    save_sparse_csr('compressedMatrix', compressed)
