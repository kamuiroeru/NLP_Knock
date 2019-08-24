#!/usr/bin/env python
import numpy
import six

n_result = 5  # number of search result to show


with open('word2vec.model', 'r') as f:
    ss = f.readline().split()
    n_vocab, n_units = int(ss[0]), int(ss[1])
    word2index = {}
    index2word = {}
    w = numpy.empty((n_vocab, n_units), dtype=numpy.float32)
    for i, line in enumerate(f):
        ss = line.split()
        # assert len(ss) == n_units + 1
        word = ss[0]
        word2index[word] = i
        index2word[i] = word
        w[i] = numpy.array([float(s) for s in ss[1:]], dtype=numpy.float32)


s = numpy.sqrt((w * w).sum(1))
w /= s.reshape((s.shape[0], 1))  # normalize
zerovec = numpy.zeros(w.shape[1])

def checkExists(instr: str):
    vec = zerovec
    try:
        vec = w[word2index[instr]]
    except KeyError:
        vec = zerovec

    return vec

def returnVec(instr: str):
    vec = zerovec
    instr = instr.strip()
    templist = instr.split(' ')
    if templist[-1] in '+-':
        print('Warning 行末の演算子は無視されます')
        templist.pop()
    while(templist):
        word = templist.pop()
        try:
            opr = templist.pop()
        except IndexError:
            opr = '+'
        if opr == '+':
            vec += checkExists(word)
        else:
            vec -= checkExists(word)

    return vec


try:
    while True:
        q = six.moves.input('>> ')
        v = returnVec(q)
        similarity = w.dot(v)
        print('query: {}'.format(q))
        count = 0
        for i in (-similarity).argsort():
            if numpy.isnan(similarity[i]):
                continue
            if index2word[i] == q:
                continue
            print('{0}: {1}'.format(index2word[i], similarity[i]))
            count += 1
            if count == n_result:
                break

except EOFError:
    pass
