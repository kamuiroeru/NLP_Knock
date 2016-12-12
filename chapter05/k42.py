from pprint import pprint

from makePickle import pickleLoad

input_sentence = pickleLoad('outchunk.pickle')

# pprint(input_sentence)

output_sentence = []
for bun in input_sentence:
    if not bun:  # bunが空（[]）の時
        continue
    strings_list = []
    for chunks in bun:
        if chunks.dst == -1:  # 係り先が無い時
            continue
        origin = ''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])  # 記号を除去
        end = ''.join([morph.surface for morph in bun[chunks.dst].morphs if not morph.pos == '記号'])  # 上に同じ
        strings_list.append(origin + end)
    string = '\t'.join(strings_list)  # タブ区切りで文字列にする
    output_sentence.append(string)

# pprint(output_sentence)

for sentence in output_sentence:
    print(sentence)
