from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:
        continue
    for chunk in bun:
        if chunk.dst == -1 \
                or '名詞' not in [morph.pos for morph in chunk.morphs] \
                or '動詞' not in [morph.pos for morph in bun[chunk.dst].morphs]:
            # 係り先が無い時 or 係り元に「名詞」を含まない時 or 係り先に「動詞」を含まない時
            continue
        print(''.join([morph.surface for morph in chunk.morphs if not morph.pos == '記号'])
              + '\t'
              + ''.join([morph.surface for morph in bun[chunk.dst].morphs if not morph.pos == '記号']))
