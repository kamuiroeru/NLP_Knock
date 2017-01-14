from k54 import load_xml


def print_person_name(word='', pos='', ner=''):
    if pos == 'NNP' and ner == 'PERSON':
        print(word)

for sentence in load_xml()['root']['document']['sentences']['sentence']:
    tokens = sentence['tokens']['token']

    # tokenが1つしか無い時の処理
    if isinstance(tokens, dict):
        print_person_name(tokens['word'], tokens['POS'], tokens['NER'])
        continue

    for t in tokens:
        print_person_name(t['word'], t['POS'], t['NER'])