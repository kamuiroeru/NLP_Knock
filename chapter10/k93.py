w2vGensim = 0
w2vMysystem = 0
N = 0

for line in open('./out92.txt'):
    N += 1
    lines = line.rstrip().split(' ')
    ans = lines[3]
    if ans == lines[4]:
        w2vGensim += 1
    if ans == lines[6]:
        w2vMysystem += 1

print('gensim: {} / {} = {:0.3f}, mysystem: {} / {} = {:0.3f}'
      .format(w2vGensim, N, w2vGensim/N, w2vMysystem, N, w2vMysystem/N))
