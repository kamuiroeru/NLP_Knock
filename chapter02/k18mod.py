import re
from operator import itemgetter
from sys import argv

lines = []
with open(argv[1], 'r') as f:
    lines = [re.split('[ \t]', line) for line in f.readlines()]

for l in sorted(lines, key=itemgetter(2), reverse=True):
    print('\t'.join(l), end='')
