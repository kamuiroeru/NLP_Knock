from sys import argv
import xml.etree.ElementTree as ET

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

tree = ET.parse(raw_text_directory)
words = tree.iter('word')
poss = tree.iter('POS')
ners = tree.iter('NER')

for obj in zip(words, poss, ners):
    obj = [ob.text for ob in obj]
    if obj[1] == 'NNP' and obj[2] == 'PERSON':
        print(obj[0])
