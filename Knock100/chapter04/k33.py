from pprint import pprint
import json

with open('out.json') as fi:
    sentences = json.load(fi)
    nouns_sa = [morpheme['surface'] for sentence in sentences for morpheme in sentence
                if len(morpheme) != 0 and morpheme['pos1'] == 'サ変接続']
    print(nouns_sa)
    print(len(nouns_sa))
