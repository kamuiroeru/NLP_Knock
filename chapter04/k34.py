import json
from time import time

with open('out.json') as fi:
    sentences = json.load(fi)

    # start = time()
    # a_and_b = [sentence[i - 1]['surface'] + morpheme['surface'] + sentence[i + 1]['surface']
    #            for sentence in sentences for i, morpheme in zip(range(len(sentence)), sentence)
    #            if morpheme['pos1'] == '連体化' and morpheme['base'] == 'の']
    # t1 = time()

    a_and_b2 = []
    for sentence in sentences:
        for i, morpheme in zip(range(len(sentence)), sentence):
            if i == 0:
                continue
            if morpheme['pos1'] == '連体化' and morpheme['base'] == 'の':
                a_and_b2.append(sentence[i - 1]['surface'] + sentence[i]['surface'] + sentence[i + 1]['surface'])
                # print(a_and_b2)
    t2 = time()
    # 4214
    # 100369

    print(a_and_b2)
    print(len(a_and_b2))
    # print('{} [sec]'.format(t1 - start))
    # print('{} [sec]'.format(t2 - t1))
