from sys import argv
import xml.etree.ElementTree as ET  # 内部モジュールのxml読み込み機能使用

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

tree = ET.parse(raw_text_directory)  # xmlファイルを読み込んでElementTreeオブジェクトに
words = tree.iter('word')  # wordの要素だけ取ってきてリストに
poss = tree.iter('POS')  # POSの（ｒｙ
ners = tree.iter('NER')  # NERの（ｒｙ

for obj in zip(words, poss, ners):
    texts = [ob.text for ob in obj]  # テキストだけほしいので抽出
    if texts[1] == 'NNP' and texts[2] == 'PERSON':
        print(texts[0])
