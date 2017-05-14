import numpy as np
import pickle

result = np.load('result.npz')
label = pickle.load(open('label.pkl', 'rb'))

print(result[label['United_States']])
