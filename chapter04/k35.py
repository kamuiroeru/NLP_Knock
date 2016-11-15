import json

with open('out.json') as fi:
    sentences = json.load(fi)
    nouns_sa = [morpheme['surface'] for sentence in sentences for morpheme in sentence
                if morpheme['pos'] == '名詞']
    nouns_sa = []
    for sentence in sentences:

        for morpheme in sentence:

    print(nouns_sa)
    print(len(nouns_sa))
