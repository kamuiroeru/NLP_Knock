import re

from makePickle import pickleLoad

for bun in pickleLoad('outchunk.pickle'):
    if len(bun) <= 1:  # bun の中の文節が1節以内のとき
        continue  # スキップ
    shortest_path_from_nouns = [None] * len(bun)  # 名詞句からの最短パスを保存
    for index, chunk in zip(range(len(bun)), bun):

        # 表示部
        if len(chunk.srcs) > 1:  # 子孫が複数いる時
            related = []  # ここまでのパス（リスト）が入る受け皿
            for src in chunk.srcs:
                if shortest_path_from_nouns[src]:  # Noneじゃないなら
                    related.append(shortest_path_from_nouns[src])
            if len(related) > 1:  # ここに係る最短パスが複数ある時
                all_pair = []
                for i, path1 in zip(range(len(related)), related):  # 全通りピックアップ
                    path2_list = related[i + 1:]
                    if path2_list:
                        for path2 in path2_list:
                            path2 = [p2.replace('X', 'Y') for p2 in path2]  # 右側のXをYに置換
                            all_pair.append([path1, path2, len(path1) + len(path2)])
                minimum_length = min([pair[2] for pair in all_pair])  # 複数の最短パス組のうち、一番短い長さをチェック
                all_pair = [[pair[0], pair[1]] for pair in all_pair if pair[2] == minimum_length]  # 長さが短いものだけで再構築
                for pair in all_pair:
                    print('{0} | {1} | {2}'.format(
                        ' -> '.join(pair[0]),
                        ' -> '.join(pair[1]),
                        ''.join([morph.surface for morph in bun[index].morphs if morph.pos != '記号'])
                    ))


        # 処理部
        if '名詞' in [morph.pos for morph in chunk.morphs]:  # 名詞が見つかれば
            noun_from = ''
            for morph in chunk.morphs:
                if not morph.pos == '記号':
                    if morph.pos == '名詞':
                        noun_from += 'X'
                    else:
                        noun_from += morph.surface
            shortest_path_from_nouns[index] = [re.sub('.+X', 'X', noun_from)]  # 最短なので（リストに入れて）置き換え
        else:  # 見つからない時
            if len(chunk.srcs) == 1:  # 一人っ子が居て
                if shortest_path_from_nouns[chunk.srcs[0]]:  # Noneじゃない時
                    temp_list = []
                    temp_list.extend(shortest_path_from_nouns[chunk.srcs[0]])  # 係り元までの最短パスに
                    temp_list.append(''.join([morph.surface for morph in chunk.morphs if '記号' != morph.pos]))  # 自分を追加して
                    shortest_path_from_nouns[index] = temp_list  # 置き換え
            if len(chunk.srcs) > 1:  # 複数子が居る時
                shortest_list = sorted(
                    [shortest_path_from_nouns[src] for src in chunk.srcs if shortest_path_from_nouns[src]],
                    key=lambda x: len(x))  # Noneを省いて、長さの短い順（パスの短い順）にソート
                if len(shortest_list) > 0:  # 全員Noneじゃなかったら
                    temp_list = []
                    temp_list.extend(shortest_list[0])  # 最短パスに
                    temp_list.append(''.join([morph.surface for morph in chunk.morphs if '記号' != morph.pos]))  # 自分を追加して
                    shortest_path_from_nouns[index] = temp_list  # 置き換え
