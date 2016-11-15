from sys import argv

with open(argv[1]) as f:
    i = 0
    for s in f:
        i += 1
        if int(argv[2]) < i:
            break
        print(s.strip())
