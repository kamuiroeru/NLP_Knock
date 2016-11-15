import json
from pprint import pprint

with open('out.json') as fi:
    pprint(json.load(fi))
