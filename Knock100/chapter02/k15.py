import sys

with open('hightemp.txt') as f:
    i = 0
    l = []
    for s in reversed(list(f)):
        i += 1
        if int(sys.argv[1]) < i:
            break
        l.insert(0, s.strip())
    print('\n'.join(l))

    # リングバッファと配列
