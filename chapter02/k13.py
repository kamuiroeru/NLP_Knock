from sys import argv


f1 = open('col1.txt')
f2 = open('col2.txt')
f3 = open(argv[1], 'w')

with f1, f2, f3:
    for s1, s2 in zip(f1, f2):
        f3.write(s1.strip() + '\t' + s2)
