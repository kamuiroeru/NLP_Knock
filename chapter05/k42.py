from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:  # bunが空（[]）の時
        continue
    strings_list = []
    for chunks in bun:
        if chunks.dst == -1:  # 係り先が無い時
            continue
        print(''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])
              + '\t'
              + ''.join([morph.surface for morph in bun[chunks.dst].morphs if not morph.pos == '記号']))