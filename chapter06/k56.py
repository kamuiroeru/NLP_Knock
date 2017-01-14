from sys import argv
import xml.etree.ElementTree as ET  # 内部モジュールのxml読み込み機能使用

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

tree = ET.parse(raw_text_directory)  # xmlファイルを読み込んでElementTreeオブジクトに
root = tree.getroot()
hoges = tree.findall('./root/document/coreference/coreference')
print(hoges)
print(root.find('.//coreference'))
coreferences = tree.iter('coreference')
for coreference in coreferences:
    for mention in coreference.mention:
        print(mention)