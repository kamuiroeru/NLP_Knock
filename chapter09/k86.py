import numpy as np
import pickle

decompMat = np.load('decompMat.npy')
label = pickle.load(open('label.pkl', 'rb'))

print(decompMat[label['United_States']])
