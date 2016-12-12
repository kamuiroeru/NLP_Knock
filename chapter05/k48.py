from sys import argv
from makePickle import pickleLoad
from graphviz import Digraph
try:
    l_number = int(argv[1])
except IndexError as e:
    l_number = 5

input_sentence = pickleLoad('outchunk.pickle')[l_number]
bun = input_sentence

if not bun:
    exit('空白行です。\n終了します。')

G = Digraph(format='png', )
G.attr('node', shape='circle')
for chunks in bun:
    if chunks.dst == -1:  # 係り先が無い時
        continue
    origin = ''.join([morph.surface for morph in chunks.morphs if not morph.pos == '記号'])  # 記号を除去
    end = ''.join([morph.surface for morph in bun[chunks.dst].morphs if not morph.pos == '記号'])  # 上に同じ
    G.edge(origin, end)  # nodeで定義しなくても繋いだらつながる
G.render('node/' + str(l_number), view=True, cleanup=True)
