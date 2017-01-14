from graphviz import Digraph
from k54 import load_xml
from sys import argv

try:
    n = int(argv[1]) - 1
except IndexError:
    n = 0

# collapsed-dependenciesは2番目
dependencies = [sentences['dependencies'][1] for sentences in load_xml()['root']['document']['sentences']['sentence']]

G = Digraph(format='png', )
G.attr('node', shape='circle')

brk = False
for dep in dependencies[n]['dep']:

    if isinstance(dep, str):  # 13文目用の処理
        dep = dependencies[n]['dep']
        brk = True

    dd, dg = dep['dependent'], dep['governor']  # 文字数削減
    G.node(dd['@idx'], dd['#text'])  # 同じ英単語でも違う場所にあったりするので
    G.node(dg['@idx'], dg['#text'])  # ちゃんとノードを作る
    G.edge(dd['@idx'], dg['@idx'], label=dep['@type'])  # 矢印作る

    if brk:  # 13文目用の処理
        break

G.render('node/' + str(n + 1), view=True, cleanup=True)
