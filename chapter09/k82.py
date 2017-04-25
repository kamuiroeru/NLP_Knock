from random import choice

with open('out82.tsv', 'w') as fo:
    for lc, line in enumerate(open('out81.txt')):
        if lc % 1000 == 0:
            print('lc: ' + str(lc))

        tokens = line.rstrip().split()
        if len(tokens) > 1:
            i = 0
            while len(tokens) > i:
                d = choice([1, 2, 3, 4, 5])  # 1 ~ 5からランダムに選択
                headindex = i - d if i - d > 0 else 0  # tokenより前を取得する時に、インデックスが負数になるのを防ぐ
                contexts = tokens[headindex: i] + tokens[i + 1: i + d + 1]  # tokenの前後d個を取得してリストに
                fo.write(tokens[i] + '\t' + '\t'.join(contexts) + '\n')
                i += 1

        # デバッグ用
        # if lc > 2000:
        #     exit(0)
