from sys import argv
import xml.etree.ElementTree as ET  # 内部モジュールのxml読み込み機能使用

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

tree = ET.parse(raw_text_directory)  # xmlファイルを読み込んでElementTreeオブジェクトに
mentions = tree.iter('mention')
for mention in mentions:
    print(mention)