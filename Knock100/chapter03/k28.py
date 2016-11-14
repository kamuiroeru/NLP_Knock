import k20
from pprint import pprint
from parse import parse
import re


def parse_wiki():
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
            dic[r[0]] = re.sub('<.*>', '', re.sub('\'|\"|\[|\]', '', r[1]))
    return dic

if __name__ == '__main__':
    pprint(parse_wiki())