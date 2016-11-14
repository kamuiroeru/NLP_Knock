from pprint import pprint
import sys
import re
import json

#     0    1         2          3          4     5     6    7   8   9
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

outer_list = []
inner_list = []
with open(sys.argv[1]) as fi:
    for line in fi.readlines():
        mapping = {}
        element = re.split('[,\t]', line.strip())
        if element[0] == 'EOS' or len(element) < 2:
            inner_list.append({})
            outer_list.append(inner_list)
            inner_list = []
            continue
        mapping['surface'] = element[0]
        mapping['base'] = element[7]
        mapping['pos'] = element[1]
        mapping['pos1'] = element[2]
        inner_list.append(mapping)
pprint(outer_list)

with open(sys.argv[2], 'w') as fo:
    json.dump(outer_list, fo)
