from k90gensim import model

keys = [line.rstrip().replace(' ', '_') for line in open('../chapter09/useList.txt')]

vectors = []
newkeys = []
for key in keys:
    try:
        vectors.append(model[key])
        newkeys.append(key)
    except KeyError:
        pass

import pickle
pickle.dump(newkeys, open('countryNames.pkl', 'wb'))
pickle.dump(vectors, open('countryVectors.pkl', 'wb'))
