import re
from collections import defaultdict
from sys import argv

lines = []
with open(argv[1], 'r') as f:
    l = [re.split('[ \t]', line)[0] for line in f.readlines()]
    dic = {k: l.count(k) for k in l}
    print('\n'.join(['{0} {1}'.format(v, k) for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)]))
