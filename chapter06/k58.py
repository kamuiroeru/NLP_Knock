from collections import defaultdict
from k54 import load_xml

# collapsed-dependenciesは2番目
dependencies = [sentences['dependencies'][1] for sentences in load_xml()['root']['document']['sentences']['sentence']]

for dependency in dependencies:

    if isinstance(dependency['dep'], dict):  # tokenが1つしか無い時は自明にスキップ
        continue

    # governor[idx]をkeyとして、valueがtuple(type, dependent, governor)のリストである辞書を作成
    check_dic = defaultdict(list)
    for dep in dependency['dep']:
        dt = dep['@type']
        dgi, ddi = dep['governor']['@idx'], dep['dependent']['@idx']
        dgt, ddt = dep['governor']['#text'], dep['dependent']['#text']
        if dt == 'nsubj' or dt == 'dobj':
            if dt == 'nsubj':
                check_dic[dgi].insert(0, int(ddi))  # 主語だったら出現位置を先頭に記録
            check_dic[dgi].append((dt, ddt, dgt))

    # [主語の出現位置, (dt, ddt, dgt), (dt, ddt, dgt)] と3つの要素が揃ってるものだけ抽出
    out_dic = {k: v for k, v in check_dic.items() if len(v) >= 3}

    # 主語の本文出現順 でソートして出力
    for k, elem in sorted(out_dic.items(), key=lambda x: x[1][0]):
        nsubj = [e[1] for e in elem[1:] if e[0] == 'nsubj'][0]
        dobj = [e[1] for e in elem[1:] if e[0] == 'dobj'][0]
        predicate = elem[1][2]  # elem[2][2] でもOK
        print(nsubj + '\t' + predicate + '\t' + dobj)
