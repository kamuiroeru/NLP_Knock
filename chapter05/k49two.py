from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bun の中の文節が1節以内のとき
        continue  # スキップ
    for chunk in bun:
        if '名詞' in [morph.pos for morph in chunk.morphs]:  # 文節に名詞が入っている時
            noun_from = ''
            for morph in chunk.morphs:
                if not morph.pos == '記号':
                    if morph.pos == '名詞':
                        noun_from += 'X'
                    else:
                        noun_from += morph.surface
            until_path = []  # 途中の経路を溜めておく
            dst_index = chunk.dst
            while dst_index != -1:  # 係り先がなくなるまで
                check_chunk = [(morph.surface, morph.pos) for morph in bun[dst_index].morphs]
                if '名詞' in [morph.pos for morph in bun[dst_index].morphs]:
                    print(' -> '.join([noun_from]+until_path+['Y']))
                until_path.append(''.join([morph.surface for morph in bun[dst_index].morphs]))
                dst_index = bun[dst_index].dst
