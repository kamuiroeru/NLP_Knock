import k20
from pprint import pprint
from parse import parse


def extract_template(page_source=k20.read_jwc_json()['イギリス']):
    dic = {}
    should_parse = False
    check = []
    for line in page_source.split('\n'):
        check.append('')
        if '基礎情報' in line:
            should_parse = True
            continue
        if should_parse:
            r = parse('|{} = {}', line)
            if r is None:
                if line == '}}':
                    break
                continue
            dic[r[0]] = r[1]
    return dic


if __name__ == '__main__':
    pprint(extract_template())
