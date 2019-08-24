import pickle

with open('pic.pickle', 'rb') as fi:
    sentence = pickle.load(fi)
    verbs = [morpheme['surface'] for morpheme in sentence if morpheme['pos'] == '動詞']
    for verb in verbs:
        print(verb)
    # print(len(verbs))
