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
            found = False  # サ変接続+'を'が見つかったかどうか
            cases = []  # 今度は係り元の[助詞の表層形, 助詞を含む文節] が入るリスト
            for chunks2 in [bun[src] for src in chunks.srcs]:
                case = [(morph.surface, morph.pos, morph.pos1) for morph in chunks2.morphs if not morph.pos == '記号']
                if case and case[-1][1] == '助詞':  # []を除去

                    # 二語以上あるか確認してから 「サ変接続+'を'」の形式を探す
                    if len(case) >= 2 and case[-1][0] == 'を' and case[-2][2] == 'サ変接続':
                        found = True  # 見つかった！！
                        predicate = case[-2][0] + case[-1][0] + predicate  # 述語を更新
                        continue
                    cases.append([case[-1][0], ''.join([c[0] for c in case])])  # [助詞の表層形, 助詞を含む文節]
            if not found or len(cases) < 1:  # サ変接続+'を'が見つからなかった or 見つかったとしても助詞が1つしか無い時
                continue
            cases.sort(key=itemgetter(0, 1))  # 助詞の表層形でソート
            print(predicate + '\t'
                  + ' '.join([case[0] for case in cases]) + '\t'  # 助詞
                  + ' '.join([case[1] for case in cases]))  # 助詞を含む文節
