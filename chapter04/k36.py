import json
from collections import Counter
# from resource import getrusage,RUSAGE_SELF

with open('out.json') as fi:
    # print(getrusage(RUSAGE_SELF).ru_maxrss)
    # sentence = json.load(fi)
    for word, count in Counter([morpheme['surface'] for morpheme in json.load(fi)]).most_common():
        print(word, count)
    # print(getrusage(RUSAGE_SELF).ru_maxrss)

