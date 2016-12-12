from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:  # bunが空（[]）の時
        continue
    for chunks in bun:
        if not chunks.srcs:
            continue
        elif '動詞' in [morph.pos for morph in chunks.morphs]:
            predicate = [morph.base for morph in chunks.morphs if morph.pos == '動詞'][0]
            cases = []
            for chunks2 in [bun[src] for src in chunks.srcs]:
                case = [morph.surface for morph in chunks2.morphs if morph.pos == '助詞']
                if case:
                    cases.extend(case)
            print(predicate + '\t' + ' '.join(sorted(cases)))
