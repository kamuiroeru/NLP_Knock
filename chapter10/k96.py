from k90gensim import model

keys = [line.rstrip().replace(' ', '_') for line in open('../chapter09/useList.txt')]

vectors = []
for key in keys:
    try:
        vectors.append(model[key])
    except KeyError:
        pass

import pickle
pickle.dump(keys, open('countryNames.pkl', 'wb'))
pickle.dump(vectors, open('countryVectors.pkl', 'wb'))
