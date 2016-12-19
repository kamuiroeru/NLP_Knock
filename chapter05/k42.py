from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    # if not bun:  # bunが空（[]）の時
    #     continue
    for chunk in bun:
        if chunk.dst == -1:  # 係り先が無い時
            continue
        print(''.join([morph.surface for morph in chunk.morphs if not morph.pos == '記号'])
              + '\t'
              + ''.join([morph.surface for morph in bun[chunk.dst].morphs if not morph.pos == '記号']))
