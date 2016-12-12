from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bunが空（[]）の時
        continue
    for chunks in bun:
        if '名詞' in [morph.pos for morph in chunks.morphs]:
            tree_path = [''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])]
            index = chunks.dst
            while index != -1:
                tree_path.append(''.join([morph.surface for morph in bun[index].morphs if not morph.pos == '記号']))
                index = bun[index].dst
            print(' -> '.join(tree_path))
