import re

from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bun の中の文節が1節以内のとき
        continue  # スキップ
    shortest_path_from_nouns = [None] * len(bun)  # 名詞句からの最短パス
    leave_node_to_root = False
    paths_from_leaf = []  # 葉から根へのパス
    paths = []  # ノードすべてから根へのパス と paths_from_leafとの対応
    sync = -1  # 対応付けるための整数を保存（引数と合わせるために-1で初期化）
    for index, chunk in zip(range(len(bun)), bun):

        # 表示部
        if len(chunk.srcs) > 1:
            related = []
            for src in chunk.srcs:
                if shortest_path_from_nouns[src]:  # Noneじゃないなら
                    related.append(shortest_path_from_nouns[src])
            if len(related) > 1:
                for i, path1 in zip(range(len(related)), related):
                    path2_list = related[i + 1:]
                    if path2_list:
                        for path2 in path2_list:
                            path2 = [p2.replace('X', 'Y') for p2 in path2]
                            print('{0} | {1} | {2}'.format(
                                ' -> '.join(path1),
                                ' -> '.join(path2),
                                ''.join([morph.surface for morph in bun[index].morphs if morph.pos != '記号'])
                            ))

        # 処理部
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            noun_from = ''
            for morph in chunk.morphs:
                if not morph.pos == '記号':
                    if morph.pos == '名詞':
                        noun_from += 'X'
                    else:
                        noun_from += morph.surface
            shortest_path_from_nouns[index] = [re.sub('.+X', 'X', noun_from)]
        elif len(chunk.srcs) == 1:
            if shortest_path_from_nouns[chunk.srcs[0]]:  # Noneじゃない時
                temp_list = []
                temp_list.extend(shortest_path_from_nouns[chunk.srcs[0]])
                temp_list.append(''.join([morph.surface for morph in chunk.morphs if '記号' != morph.pos]))
                shortest_path_from_nouns[index] = temp_list
        elif len(chunk.srcs) > 1:
            shortest_list = sorted(
                [shortest_path_from_nouns[src] for src in chunk.srcs if shortest_path_from_nouns[src]],
                key=lambda x: len(x))
            if len(shortest_list) > 0:
                temp_list = []
                temp_list.extend(shortest_list[0])
                temp_list.append(''.join([morph.surface for morph in chunk.morphs if '記号' != morph.pos]))
                shortest_path_from_nouns[index] = temp_list
