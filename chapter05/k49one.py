import re

from makePickle import pickleLoad

# def count_path_from_leaf(i, lis):
#     count = 0
#     for l in lis:
#         if i in l:
#             count += 1
#     return count
#
#
# # node_has_childrenの子孫であるノードすべてからnode_has_children直前までのパスのリストを返す
# def create_prev_nodes(node_has_children, lis):
#     ret_list = []
#     for l, sync in lis:
#         if node_has_children in l:
#             path = []
#             for i in l:
#                 if i == node_has_children:
#                     break
#                 path.append(i)
#             ret_list.append((path, sync))
#     return ret_list
#
#
# def print_related(srcs, spfn):
#     related = []
#     for src in srcs:
#         if spfn[src]:
#             related.append(spfn[srcs])


if __name__ == '__main__':
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
                    #
                    #     path = [i]
                    #     index = chunk.dst
                    #     while index != -1:
                    #         path.append(index)
                    #         index = bun[index].dst
                    #     if not chunk.srcs:  # 係り元が無い時：葉からのパス
                    #         paths_from_leaf.append(path)
                    #         sync += 1
                    #     paths.append((path, sync))
                    #
                    # for index in range(len(bun)):
                    #     if leave_node_to_root:  # これより先には合流地点が無い時
                    #         break
                    #     count = count_path_from_leaf(index, paths_from_leaf)  # 葉からのパスが何本あるか
                    #     if count >= 2:  # 2本以上なら合流地点である
                    #         if count == len(paths_from_leaf):  # 一番根に近い合流地点
                    #             leave_node_to_root = True
                    #         shortest_list = [None] * count
                    #         for path, sync in create_prev_nodes(index, paths):
                    #             related_chunks = []
                    #             for times, index2 in zip(range(len(path)), path):
                    #                 if times == 0:
                    #                     if '名詞' in [morph.pos for morph in bun[index2].morphs]:  # 文節に名詞が入っている時
                    #                         noun_from = ''
                    #                         for morph in bun[index2].morphs:
                    #                             if not morph.pos == '記号':
                    #                                 if morph.pos == '名詞':
                    #                                     noun_from += 'X'
                    #                                 else:
                    #                                     noun_from += morph.surface
                    #                         related_chunks.append(re.sub('.+X', 'X', noun_from))  # Xの重なりとかをまとめて追加
                    #                     else:
                    #                         break  # パスの始まりの文節が名詞を含まなかったらbreak
                    #                 else:
                    #                     related_chunks.append(''.join([morph.surface for morph in bun[index2].morphs]))
                    #             if related_chunks:
                    #                 shortest_list[sync] = related_chunks
                    #         shortest_list = [shortest for shortest in shortest_list if shortest]  # None以外を摘出
                    #
                    #         if len(shortest_list) > 1:
                    #             for i, path1 in zip(range(len(shortest_list)), shortest_list):
                    #                 path2_list = shortest_list[i + 1:]
                    #                 if path2_list:
                    #                     for path2 in path2_list:
                    #                         path2 = [p2.replace('X', 'Y') for p2 in path2]
                    #                         print('{0} | {1} | {2}'.format(
                    #                             ' -> '.join(path1),
                    #                             ' -> '.join(path2),
                    #                             ''.join([morph.surface for morph in bun[index].morphs if morph.pos != '記号'])
                    #                         ))
