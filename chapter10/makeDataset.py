import pickle
from os.path import exists
import numpy as np

def createVocab():
    print('making_word2index')
    wordSet = set([word for line in open('../chapter09/out81.txt') for word in line.rstrip().split(' ')])
    word2index = {k: lc for lc, k in enumerate(wordSet)}
    print('saveing_word2index')
    pickle.dump(word2index, open('word2index.pkl', 'wb'))
    print('done')
    return word2index

def createWords(word2index):
    print('making_words')
    words = np.array([word2index[word] for line in open('../chapter09/out81.txt') for word in line.rstrip().split(' ')],
                     dtype=np.int32)
    print('saving_words')
    pickle.dump(words, open('words.pkl', 'wb'))
    print('done')
    return words


if exists('word2index.pkl'):
    word2index = pickle.load(open('word2index.pkl', 'rb'))
else:
    word2index = createVocab()

if exists('words.pkl'):
    words = pickle.load(open('words.pkl', 'rb'))
else:
    words = createWords(word2index)
