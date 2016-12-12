from operator import itemgetter

from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:  # bunが空（[]）の時
        continue
    for chunks in bun:
        if not chunks.srcs:
            continue
        elif '動詞' in [morph.pos for morph in chunks.morphs]:
            predicate = [morph.base for morph in chunks.morphs if morph.pos == '動詞'][0]
            cases = []  # 今度は係り元の[助詞の表層形, 助詞を含む文節] が入るリスト
            for chunks2 in [bun[src] for src in chunks.srcs]:
                case = [(morph.surface, morph.pos) for morph in chunks2.morphs if not morph.pos == '記号']
                if case and case[-1][1] == '助詞':
                    cases.append([case[-1][0], ''.join([c[0] for c in case])])  # [助詞の表層形, 助詞を含む文節]
            cases.sort(key=itemgetter(0, 1))  # 助詞の表層形でソート
            print(predicate + '\t'
                  + ' '.join([case[0] for case in cases]) + '\t'  # 助詞
                  + ' '.join([case[1] for case in cases]))  # 助詞を含む文節
