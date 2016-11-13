import re

with open('hightemp.txt', 'r') as f:
    # uniq = set([line.split('\t')[0] for line in f.readlines()])
    uniq = {re.split('[ \t]+', line)[0] for line in f.readlines()}

print(uniq)
