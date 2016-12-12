from makePickle import pickleLoad

input_sentence = pickleLoad('outchunk.pickle')

output_sentence = []
for bun in input_sentence:
    if not bun:
        continue
    strings_list = []
    for chunks in bun:
        if chunks.dst == -1 \
                or '名詞' not in [morph.pos for morph in chunks.morphs] \
                or '動詞' not in [morph.pos for morph in bun[chunks.dst].morphs]:
            # 係り先が無い時 or 係り元に「名詞」を含まない時 or 係り先に「動詞」を含まない時
            continue
        origin = ''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])
        end = ''.join([morph.surface for morph in bun[chunks.dst].morphs if not morph.pos == '記号'])
        strings_list.append(origin + end)
    string = '\t'.join(strings_list)
    output_sentence.append(string)

# pprint(output_sentence)

for sentence in output_sentence:
    print(sentence)
