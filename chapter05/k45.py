from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:  # bunが空（[]）の時
        continue
    for chunk in bun:
        if not chunk.srcs:
            continue
        elif '動詞' in [morph.pos for morph in chunk.morphs]:
            predicate = [morph.base for morph in chunk.morphs if morph.pos == '動詞'][0]
            cases = []  # 係り元の助詞が入るリスト
            for chunks2 in [bun[src] for src in chunk.srcs]:  # 係り元全部に対して文節ごとに

                # 記号を取り除いて（表層形, 品詞）のタプル in リストを作る
                case = [(morph.surface, morph.pos) for morph in chunks2.morphs if not morph.pos == '記号']
                if case and case[-1][1] == '助詞':  # 末尾が助詞だった場合（caseが[]の場合を弾くために case and かます）
                    cases.append(case[-1][0])  # その助詞の表層形を取り出してリストに
            if cases:
                print(predicate + '\t' + ' '.join(sorted(cases)))
