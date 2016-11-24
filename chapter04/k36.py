import json
from collections import Counter

# from resource import getrusage,RUSAGE_SELF
from operator import itemgetter

with open('out.json') as fi:
    # print(getrusage(RUSAGE_SELF).ru_maxrss)
    sentence = json.load(fi)
    total = len(sentence)
    for word, count in sorted(Counter([morpheme['base'] for morphbeme in sentence]).most_common(), key=itemgetter(1,0), reverse=True):
        print(word, count/total)
        # print(word)
        # print(getrusage(RUSAGE_SELF).ru_maxrss)
