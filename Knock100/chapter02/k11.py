from sys import argv

with open(argv[1]) as f:
    for s in f:
        print(s.replace('\t', ' ').strip())
