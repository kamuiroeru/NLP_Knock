import json

with open('out.json') as fi:
    sentences = json.load(fi)
    nouns_sa = [morpheme['surface'] for sentence in sentences for morpheme in sentence
                if morpheme['pos1'] == 'サ変接続']
    for noun_sa in nouns_sa:
        print(noun_sa)
    # print(len(nouns_sa))
