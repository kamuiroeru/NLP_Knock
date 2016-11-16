import json

with open('out.json') as fi:
    sentences = json.load(fi)
    verbs = [morpheme['surface'] for sentence in sentences for morpheme in sentence
             if morpheme['pos'] == '動詞' and morpheme['surface'] == morpheme['base']]
    print(verbs)
    # print(len(verbs))