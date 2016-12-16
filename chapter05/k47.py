from operator import itemgetter

from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if not bun:  # bunが空（[]）の時
        continue
    for chunk in bun:
        if not chunk.srcs:
            continue
        elif '動詞' in chunk.morphs[0].pos:
            predicate = chunk.morphs[0].base  # 動詞の最左
            found = False  # サ変接続+'を'が見つかったかどうか
            cases = []  # 今度は係り元の[助詞の表層形, 助詞を含む文節] が入るリスト
            for chunk2 in [bun[src] for src in chunk.srcs]:
                case = [morph for morph in chunk2.morphs if not morph.pos == '記号']  # chunk2.morphsを記号抜きで再構築
                if case and case[-1].pos == '助詞':  # caseが[]の場合を考慮

                    # 二語以上あるか確認してから 「サ変接続+'を'」の形式を探す
                    if len(case) >= 2 and case[-1].surface == 'を' and case[-2].pos1 == 'サ変接続':
                        found = True  # 見つかった！！
                        predicate = case[-2].base + case[-1].surface + predicate  # 述語を更新
                        continue
                    cases.append([case[-1].surface, ''.join([morph.surface for morph in case])])  # [助詞の表層形, 助詞を含む文節]
            if not found or len(cases) < 1:  # サ変接続+'を'が見つからなかった or 見つかったとしても助詞が1つしか無い時
                continue
            cases.sort(key=itemgetter(0, 1))  # 助詞の表層形でソート
            print(predicate + '\t'
                  + ' '.join([case[0] for case in cases]) + '\t'  # 助詞
                  + ' '.join([case[1] for case in cases]))  # 助詞を含む文節
