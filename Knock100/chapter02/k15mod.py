from sys import argv

with open(argv[1]) as f:
    for line in f.readlines()[-int(argv[2]):]:
        print(''.join(line.rstrip()))

    # リングバッファと配列

