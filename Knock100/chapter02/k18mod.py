import re
from operator import itemgetter

lines = []
with open('hightemp.txt', 'r') as f:
    lines = [re.split('[ \t]', line) for line in f.readlines()]

for l in sorted(lines, key=itemgetter(2), reverse=True):
    print('\t'.join(l), end='')
