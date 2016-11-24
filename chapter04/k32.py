import json

with open('out.json') as fi:
    sentence = json.load(fi)
    verbs = [morpheme['base'] for morpheme in sentence if morpheme['pos'] == '動詞']
    for verb in verbs:
        print(verb)
        # print(len(verbs))
