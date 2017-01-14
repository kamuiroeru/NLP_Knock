from collections import defaultdict

from k54 import load_xml

# collapsed-dependenciesは2番目
dependencies = [sentences['dependencies'][1] for sentences in load_xml()['root']['document']['sentences']['sentence']]

for dependency in dependencies:

    check_dic = defaultdict(list)
    if isinstance(dependency['dep'], dict):  # tokenが1つしか無い時は自明にスキップ
        continue
    for lc, dep in enumerate(dependency['dep']):
        dt = dep['@type']
        dgi = dep['governor']['@idx']
        dgt, ddt = dep['governor']['#text'], dep['dependent']['#text']
        if dt == 'nsubj' or dt == 'dobj':
            # print(dgt, dt, ddt)
            check_dic[dgi].append((lc, dt, ddt, dgt))

    output_dic = check_dic
    for k, elem in sorted(check_dic.items(), key=lambda x: x[0]):
        if len(elem) >= 2:
            index = min([e[0] for e in elem])
            nsubj = [e[2] for e in elem if e[1] == 'nsubj'][0]
            dobj = [e[2] for e in elem if e[1] == 'dobj'][0]
            predicate = elem[0][3]
            print(nsubj + '\t' + predicate + '\t' + dobj)
