import re
from collections import defaultdict
from makePickle import pickleLoad

import pandas as pd

from MyClass import Morph
from MyClass import Chunk


def create_chunk(cabocha_text_lattice='neko.txt.cabocha'):
    outer_list = []
    inner_list = []
    temp_dic = defaultdict(list)
    chunk = Chunk()
    index = -1
    with open(cabocha_text_lattice) as f:
        for line in f:
            status = line.split(' ')
            if len(status) == 5:  # latticeの行なら
                chunk.srcs = temp_dic[str(index)]
                inner_list.append(chunk)
                index += 1
                chunk = Chunk()
                chunk.dst = int(status[2][:-1])  # D抜いてintにキャスト
                temp_dic[str(chunk.dst)].append(index)  # 係り元を集計
            else:
                if 'EOS' in line:  # EOSの時
                    chunk.srcs = temp_dic[str(index)]
                    inner_list.append(chunk)
                    outer_list.append(inner_list[1:])
                    chunk = Chunk()
                    inner_list = []
                    temp_dic = defaultdict(list)
                    index = -1
                else:
                    elements = re.split('[,\t]', line.rstrip())
                    morph = Morph()
                    morph.surface = elements[0]
                    morph.base = elements[7]
                    morph.pos = elements[1]
                    morph.pos1 = elements[2]
                    chunk.morphs.append(morph)
    return outer_list


if __name__ == '__main__':
    chunk8 = pickleLoad('outchunk.pickle')[7]
    df = pd.DataFrame(
        [[''.join([morph.surface for morph in chunk.morphs]), str(chunk.dst)] for chunk in chunk8],
        columns=['文節', '係り先'])
    print(df)
