import sys, os

os.system('rm -f spl*')

with open('hightemp.txt') as f:
    i = 1
    il = 0
    for s in f:
        if int(sys.argv[1]) > il:
            il += 1
        else:
            il = 1
            i += 1
        with open('spl' + str(i) + '.txt', 'a') as fo:
            fo.write(s)
