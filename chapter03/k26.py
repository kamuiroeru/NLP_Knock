import k20
from pprint import pprint
from parse import parse
import re

dic = {}
shouldParse = False
check = []
for line in k20.read_jwc_json()['イギリス'].split('\n'):
    check.append('')
    if '基礎情報' in line:
        shouldParse = True
        continue
    if shouldParse:
        r = parse('|{} = {}', line)
        if r is None:
            if line == '}}':
                break
            continue
        dic[r[0]] = re.sub('\'|\"', '', r[1])

pprint(dic)

# 強調マークアップは1行だけ存在した
