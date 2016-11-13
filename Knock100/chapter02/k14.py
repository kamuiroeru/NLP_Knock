import sys

with open('hightemp.txt') as f:
    i = 0
    for s in f:
        i += 1
        if int(sys.argv[1]) < i:
            break
        print(s.strip())
