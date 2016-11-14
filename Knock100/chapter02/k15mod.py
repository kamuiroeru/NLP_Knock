import sys

with open('hightemp.txt') as f:
    for line in f.readlines()[-int(sys.argv[1]):]:
        print(''.join(line.rstrip()))

    # リングバッファと配列

