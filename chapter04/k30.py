from pprint import pprint
import sys
import re


#     0    1         2          3          4     5     6    7   8   9
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

def load_mecab(strin=''):
    outer_list = []  # 全文リスト（要素は１文リスト）
    inner_list = []  # １文リスト（要素は
    with open(strin) as fi:
        for line in fi.readlines():
            mapping = {}
            element = re.split('[,\t]', line.strip())
            if element[0] != 'EOS':
                mapping['surface'] = element[0]  # 表層形
                mapping['base'] = element[7]  # 原形（基本形）
                mapping['pos'] = element[1]  # 品詞
                mapping['pos1'] = element[2]  # 品詞細分類1
                inner_list.append(mapping)
            if len(inner_list) > 1 and inner_list[-1]['surface'] == '。':
                inner_list.pop()
                outer_list.append(inner_list)
                inner_list = []
    return outer_list


if __name__ == '__main__':
    pprint(load_mecab(sys.argv[1]))
