import pickle
from scipy.sparse import lil_matrix, csr_matrix, linalg
# from scipy import io
import numpy as np
# from itertools import combinations
import multiprocessing as mp
from time import time


def save_sparse_csr(filename, array):
    np.savez(filename, data=array.data, indices=array.indices,
             indptr=array.indptr, shape=array.shape)


def load_sparse_csr(filename):
    loader = np.load(filename)
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),
                      shape=loader['shape'])


if __name__ == '__main__':
    start = time()
    print('Loading, Pickling')
    label = {v: lc for lc, v in enumerate(pickle.load(open('./t_Dic.pkl', 'rb')))}

    pickle.dump(label, open('label.pkl', 'wb'))

    matrix = lil_matrix((len(label), len(label)))
    cov_matrix = lil_matrix((len(label), len(label)))

    for k, v in pickle.load(open('./ppmiDic.pkl', 'rb')).items():
        matrix[label[k[0]], label[k[1]]] = v

    print('Done {} [sec]'.format(time() - start))

    def retCov(i, j):
        if matrix[j].data[0]:
            x = matrix[i].toarray()[0]
            y = matrix[j].toarray()[0]
            deviation_x = x - x.mean()
            deviation_y = y - y.mean()
            return np.average(np.multiply(deviation_x, deviation_y)), i, j
        else:
            return 0

    num_of_process = 8
    pool = mp.Pool(num_of_process)
    print('pool {} process'.format(num_of_process))
    start = time()
    print('start culiculate_Cov')
    for i in range(len(label)):
        print(i, '{} [sec]'.format(time() - start))
        if matrix[i].data[0]:
            subVars = pool.starmap(retCov, [(i, j) for j in range(i + 1, len(label))])
            for subVar in subVars:
                if subVar:
                    data, i, j = subVar[0], subVar[1], subVar[2]
                    cov_matrix[i, j] = data
                    cov_matrix[j, i] = data
    pool.terminate()
    print('Done {} [sec]'.format(time() - start))

    # titanで16分かかる
    start = time()
    pool = mp.Pool(num_of_process)
    print('start culculate_Cov_taikaku')

    def retVar(i):
        if i % 100000 == 0:
            print(i)
        if matrix[i].data[0]:
            return np.var(matrix[i].toarray()[0]), i
        else:
            return 0
    retVars = pool.map(retVar, range(len(label)))
    pool.terminate()
    for retr in retVars:
        if retr:
            data, i = retr[0], retr[1]
            cov_matrix[i] = data
    print('Done {} [sec]'.format(time() - start))

    cov_matrix = cov_matrix.tocsr()

    start = time()
    print('saving cov_matrix')
    save_sparse_csr('cov_matrix', cov_matrix)
    print('Done {} [sec]'.format(time() - start))

    print('元の行列:{} × {}'.format(*matrix.shape))

    start = time()
    print('compressing')
    save_sparse_csr('cov_matrix.mat', cov_matrix)
    E, V = linalg.eigs(matrix, k=300)

    # compressed = matrix.dot(V)
    compressed = matrix.dot(lil_matrix(V).tocsr())

    print('Done {} [sec]'.format(time() - start))
    print('圧縮後の行列:{} × {}'.format(*compressed.shape))

    # pickle.dump(compressed, open('compressedMatrix.pkl', 'wb'))
    save_sparse_csr('compressedMatrix', compressed)

# for label in np.array(subVars).T[0].nonzero()[0]:
#     if subVar:
#         elem = subVars[label]
#         data, i, j = elem[0], elem[1], elem[2]
#         cov_matrix[i, j] = data
#         cov_matrix[j, i] = data
