import json
from pprint import pprint

with open('out.json') as fi:
    sentence = json.load(fi)
    nouns_sa = [morpheme for morpheme in sentence if morpheme['pos1'] == 'サ変接続']
    # pprint(nouns_sa)
    for noun_sa in nouns_sa:
        pprint(noun_sa)
    # print(len(nouns_sa))
