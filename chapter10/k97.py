# coding: utf-8

import numpy as np
from sklearn.cluster import KMeans
import pickle

keys = pickle.load(open('countryNames.pkl', 'rb'))
vectors = pickle.load(open('countryVectors.pkl', 'rb'))

k = 5
pred = KMeans(n_clusters=k).fit_predict(vectors)
claster = {}
for i in range(k):
    claster[i] = [keys[j] for j in np.where(pred == i)[0]]

from pprint import pprint
pprint(claster)

import json
json.dump(claster, open('KMeans.json', 'w'))
