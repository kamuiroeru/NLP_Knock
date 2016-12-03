from pprint import pprint
import sys
import json

import pickle

import k30true

#     0    1         2          3          4     5     6    7   8   9
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
dic = k30true.load_mecab(sys.argv[1])
pprint(dic)
with open(sys.argv[2], 'w') as fo:
    json.dump(dic, fo)
    # pickle.dump(dic, open('pic.pickle', 'wb'))
