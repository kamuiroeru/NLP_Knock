from pprint import pprint
from sys import argv
import xml.etree.ElementTree as ET  # 内部モジュールのxml読み込み機能使用
from graphviz import Digraph

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

tree = ET.parse(raw_text_directory)  # xmlファイルを読み込んでElementTreeオブジェクトに

sentences = []
for dependencie in tree.iter('dependencies'):
    if dependencie.attrib['type'] == 'collapsed-dependencies':
        sentence = []
        for dep in dependencie:
            sentence.append([(d.text, d.get('idx')) for d in dep])
        sentences.append(sentence)
pprint(sentences)

G = Digraph(format='png', )
G.attr('node', shape='circle')
for dep in sentences[0]:
    h = [d[0] for d in dep][::-1]
    G.edge(*h)

G.render('node/' + str(0), view=True, cleanup=True)
