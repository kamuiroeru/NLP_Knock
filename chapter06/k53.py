import json
from pprint import pprint

import corenlp

corenlp_dir = '/usr/local/lib/stanford-corenlp-full-2016-10-31/'
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir, properties='hoge.properities')

obj = parser.parse('Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of humani-computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.')
print(obj)
# result_json = json.loads(parser.parse('Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of humani-computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.'))
# pprint(result_json)
