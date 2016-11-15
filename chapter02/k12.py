import re
from sys import argv


f = open(argv[1])
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')

with f, f1, f2:
    # l = []
    # for s in f.readlines():
    #     l.append(s.replace('\t', ' ').split(' '))
    # for sl in l:
    for sl in [re.split(r'[ \t]+', s) for s in f]:
        f1.write(sl[0] + '\n')
        f2.write(sl[1] + '\n')
