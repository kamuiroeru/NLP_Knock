import json

with open('out.json') as fi:
    sentence = json.load(fi)
    nouns_sequences = []
    is_continuing = False
    nouns_sequence = []
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            is_continuing = True
        else:
            if len(nouns_sequence) >= 2:  # 2単語以上繋がったものだけ取り出す
                nouns_sequences.append(''.join(nouns_sequence))
            nouns_sequence = []
            is_continuing = False
        if is_continuing:
            nouns_sequence.append(morpheme['surface'])

for nouns_sequence in nouns_sequences:
    print(nouns_sequence)
    # print(len(nouns_sequences))
