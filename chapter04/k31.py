import json

with open('out.json') as fi:
    sentences = json.load(fi)
    verbs = [morpheme['surface'] for sentence in sentences for morpheme in sentence
             if len(morpheme) != 0 and morpheme['pos'] == '動詞']
    print(verbs)
    # print(len(verbs))
