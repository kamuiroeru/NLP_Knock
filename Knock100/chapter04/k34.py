from pprint import pprint
import json

with open('out.json') as fi:
    sentences = json.load(fi)
    # nouns_sa = [sentence[i - 1]['surface'] + morpheme['surface'] + sentence[i + 1]['surface']
    #             for sentence in sentences for i, morpheme in zip(range(len(sentence)), sentence)
    #             if len(morpheme) != 0 and morpheme['pos1'] == '連体化' and morpheme['base'] == 'の']
    nouns_sa = []
    j = 0
    for sentence in sentences:
        for i, morpheme in zip(range(len(sentence)), sentence):
            j += 1
            if len(morpheme) != 0 and morpheme['pos1'] == '連体化' and morpheme['base'] == 'の':
                nouns_sa.append(sentence[i - 1]['surface'] + sentence[i]['surface'] + sentence[i + 1]['surface'])
                print(sentence[i - 1]['surface'] + sentence[i]['surface'] + sentence[i + 1]['surface'])
                # print(j)
    print(nouns_sa)
    print(len(nouns_sa))

    # 104148行目
