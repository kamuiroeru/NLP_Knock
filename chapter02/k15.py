from sys import argv

with open(argv[1]) as f:
    i = 0
    l = []
    for s in reversed(list(f)):
        i += 1
        if int(argv[2]) < i:
            break
        l.insert(0, s.strip())
    print('\n'.join(l))

    # リングバッファと配列
