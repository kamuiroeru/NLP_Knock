import pickle

dic = pickle.load(open('xml.pickle', 'rb'))

sentences = dic['root']['document']['sentences']

# sentence_list[sentenceIndex][tokenIndex]で任意の単語が取得できるようなリストを作成
sentence_list = [[]]  # インデックス調整の為
for sentence in sentences['sentence']:
    # print(sentence['@id'])
    token_list = ['']  # インデックス調整の為
    if isinstance(sentence['tokens']['token'], dict):
        # print(sentence['tokens']['token']['word'])
        token_list.append(sentence['tokens']['token']['word'])
    else:
        for token in sentence['tokens']['token']:
            # print(token['word'])
            token_list.append(token['word'])
    sentence_list.append(token_list)

for core in dic['root']['document']['coreference']['coreference']:
    rep = ''
    for mention in core['mention']:
        if '@representative' in mention:
            # print(mention['@representative'])
            rep = (mention['text'])
        else:
            sent = int(mention['sentence'])
            start = int(mention['start'])
            end = int(mention['end'])
            sentence_list[sent][start] = '「 ' + rep + ' ( ' + sentence_list[sent][start]
            sentence_list[sent][end] = ')」' + sentence_list[sent][end]

for token_l in sentence_list[1:]:
    print(' '.join(token_l[1:]))
    # for token in token_l:
    #     print(token[1]+token[0], end='')
    # print()
