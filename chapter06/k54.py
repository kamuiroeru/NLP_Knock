import pickle

dic = pickle.load(open('xml.pickle', 'rb'))

sentences = dic['root']['document']['sentences']['sentence']

for sentence in sentences:
    tokens = sentence['tokens']['token']
    if isinstance(tokens, dict):
        print(tokens['word'], tokens['lemma'], tokens['POS'])
        continue
    for t in tokens:
        print(t['word'], t['lemma'], t['POS'])
