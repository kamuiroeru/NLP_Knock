import json

with open('out.json') as fi:
    sentences = json.load(fi)
    verbs = [morpheme['surface'] for sentence in sentences for morpheme in sentence
             if morpheme['pos'] == '動詞']
    print(verbs)
    # print(len(verbs))
