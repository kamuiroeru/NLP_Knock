import re
from itertools import combinations
from makePickle import pickleLoad


for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bun の中の文節が1節以内のとき
        continue  # スキップ
    paths_from_leaf = []  # 葉から根へのパス
    nouns = []
    for i, chunk in zip(range(len(bun)), bun):
        if not chunk.srcs:
            index = i
            path = []
            while index != -1:
                path.append(index)
                index = bun[index].dst
            paths_from_leaf.append(path)
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            noun_from = ''
            for morph in bun[i].morphs:
                if not morph.pos == '記号':
                    if morph.pos == '名詞':
                        noun_from += 'X'
                    else:
                        noun_from += morph.surface
            nouns.append([i, re.sub('.+X', 'X', noun_from)])  # Xの重なりとかをまとめて追加

    for node1, node2 in combinations(nouns, 2):
        two_nodes_are_on_the_same_path = False
        pfl_index1 = 0
        pfl_index2 = 0
        for pfl_index, lis in zip(range(len(paths_from_leaf)), paths_from_leaf):
            if node1[0] in lis and node2[0] in lis:
                two_nodes_are_on_the_same_path = True  # 同じパス上にあります。
                break
            elif node1[0] in lis:
                pfl_index1 = pfl_index
            elif node2[0] in lis:
                pfl_index2 = pfl_index
        if not two_nodes_are_on_the_same_path:
            path1 = paths_from_leaf[pfl_index1]
            path2 = paths_from_leaf[pfl_index2]
            meeting_node = [node for node in path1 if node in path2][0]

            shortest_path1 = [node1[1]]
            next_index1 = bun[node1[0]].dst
            while next_index1 != meeting_node:
                shortest_path1.append(''.join([morph.surface for morph in bun[next_index1].morphs if morph.pos != '記号']))
                next_index1 = bun[next_index1].dst

            shortest_path2 = [node2[1]]
            next_index2 = bun[node2[0]].dst
            while next_index2 != meeting_node:
                shortest_path2.append(''.join([morph.surface for morph in bun[next_index2].morphs if morph.pos != '記号']))
                next_index2 = bun[next_index2].dst
            print('{0} | {1} | {2}'.format(
                ' -> '.join(shortest_path1),
                ' -> '.join(shortest_path2).replace('X', 'Y'),
                ''.join([morph.surface for morph in bun[meeting_node].morphs if morph.pos != '記号'])
            ))
