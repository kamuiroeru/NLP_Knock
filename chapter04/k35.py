import json

with open('out.json') as fi:
    sentences = json.load(fi)
    # nouns_sequences = [ ''.join([morpheme['surface'] for morpheme in sentence if morpheme['pos'] == '名詞'])
    #                    for sentence in sentences]
    nouns_sequences = []
    is_continuing = False
    for sentence in sentences:
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

    print(nouns_sequences)
    print(len(nouns_sequences))
