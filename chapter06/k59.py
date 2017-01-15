from pprint import pprint

from k54 import load_xml

parse_strings = [sentences['parse'] for sentences in load_xml()['root']['document']['sentences']['sentence']]

pprint(parse_strings)
