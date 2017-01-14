import pickle


def load_xml():
    return pickle.load(open('xml.pickle', 'rb'))

if __name__ == '__main__':
    for sentence in load_xml()['root']['document']['sentences']['sentence']:
        tokens = sentence['tokens']['token']

        # tokenが1つしか無い時の処理
        if isinstance(tokens, dict):
            print(tokens['word'], tokens['lemma'], tokens['POS'])
            continue

        for t in tokens:
            print(t['word'], t['lemma'], t['POS'])