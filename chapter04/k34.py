import json
from time import time

with open('out.json') as fi:
    sentence = json.load(fi)

    # start = time()
    # a_and_b = [sentence[i - 1]['surface'] + morpheme['surface'] + sentence[i + 1]['surface']
    #            for sentence in sentences for i, morpheme in zip(range(len(sentence)), sentence)
    #            if morpheme['pos1'] == '連体化' and morpheme['base'] == 'の']
    # t1 = time()

    a_and_b2 = []
    for i, morpheme in zip(range(len(sentence)), sentence):
        if morpheme['pos'] == '名詞':
            if sentence[i + 1]['surface'] == 'の':
                if sentence[i + 2]['pos'] == '名詞':
                    a_and_b2.append(
                        ''.join([mor['surface'] for mor in [sentence[i], sentence[i + 1], sentence[i + 2]]]))

for a_b in a_and_b2:
    print(a_b)
    # print(len(a_and_b2))
    # print('{} [sec]'.format(t1 - start))
    # print('{} [sec]'.format(t2 - t1))
