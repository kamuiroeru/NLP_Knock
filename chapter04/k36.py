import json
from collections import Counter

# from resource import getrusage,RUSAGE_SELF

with open('out.json') as fi:
    # print(getrusage(RUSAGE_SELF).ru_maxrss)
    sentence = json.load(fi)
    total = len(sentence)
    for word, count in Counter([morpheme['base'] for morpheme in sentence]).most_common():
        print(word, count/total)
        # print(word)
        # print(getrusage(RUSAGE_SELF).ru_maxrss)
