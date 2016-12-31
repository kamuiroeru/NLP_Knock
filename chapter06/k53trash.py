import json
from pprint import pprint
from sys import argv
import xmltodict

import corenlp


corenlp_dir = '/usr/local/lib/stanford-corenlp-full-2016-10-31/'

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt'

str = ''
with open(raw_text_directory) as f:
    for line in f:
        str += line.rstrip()
# print(str)

parser = corenlp.StanfordCoreNLP(corenlp_dir)
parsed = xmltodict.unparse(json.loads(parser.parse(str)))

with open('hoge.txt', 'w') as f:
    f.write(parsed)
# parsed = xmltodict.unparse(json.loads(parser.parse('Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.')))

# print(parsed)

# for p in parsed:
#     print(p)
