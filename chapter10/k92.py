from k90gensim import model

with open('./out92.txt', 'w') as f:
    for line in open('./out91.txt'):
        col = line.rstrip().split(' ')
        pos, neg = [col[2], col[1]], [col[0]]
        out = model.most_similar(topn=1, positive=pos, negative=neg)
        outstr = col + [out[0][0], str(out[0][1])]
        print(outstr)
        f.write(' '.join(outstr) + '\n')
