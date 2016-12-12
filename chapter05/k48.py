from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bun の中の文節が1節以内のとき
        continue  # スキップ
    for chunks in bun:
        if '名詞' in [morph.pos for morph in chunks.morphs]:  # 文節に名詞が入っている時
            tree_path = [''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])]
            index = chunks.dst
            while index != -1:  # 係り先がなくなるまで
                tree_path.append(''.join([morph.surface for morph in bun[index].morphs if not morph.pos == '記号']))
                index = bun[index].dst
            print(' -> '.join(tree_path))
