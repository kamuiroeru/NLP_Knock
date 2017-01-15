from k54 import load_xml
import re

# sentence_list[sentenceIndex][tokenIndex]で任意の単語が取得できるようなリストを作成
sentence_list = [[]]  # インデックス調整の為予め1つ要素を入れておく

for sentence in load_xml()['root']['document']['sentences']['sentence']:
    token_list = ['']  # インデックス調整の為（ｒｙ
    if isinstance(sentence['tokens']['token'], dict):
        token_list.append(sentence['tokens']['token']['word'])
    else:
        for token in sentence['tokens']['token']:
            token_list.append(token['word'])
    sentence_list.append(token_list)

for core in load_xml()['root']['document']['coreference']['coreference']:
    rep = ''
    for mention in core['mention']:
        if '@representative' in mention:  # 代表参照表現なら文字列を取得
            rep = (mention['text'])
        else:
            sent = int(mention['sentence'])
            start = int(mention['start'])
            end = int(mention['end'])

            # 参照表現の先頭に '「 [代表表現] ( ' を追加
            sentence_list[sent][start] = '「 ' + rep + ' ( ' + sentence_list[sent][start]

            # 参照表現の 1つ後ろ の先頭に ')」' を追加
            sentence_list[sent][end] = ')」 ' + sentence_list[sent][end]

for token_l in sentence_list[1:]:
    outStr = re.sub(r' ([,.;:?!])', r'\1', ' '.join(token_l[1:]))  # カンマやピリオドの前の空白を削除
    outStr = outStr.replace('-LRB- ', '(').replace(' -RRB-', ')')  # ()に戻す
    print(outStr)
