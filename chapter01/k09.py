from random import shuffle

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
lo = []
for word in s.split(' '):
    if len(word) > 4:
        head, mid, tail = word[0], word[1:-1], word[-1]
        mid_l = list(mid)
        shuffle(mid_l)
        shuffled = ''.join(mid_l)
        lo.append(head + shuffled + tail)
    else:
        lo.append(word)
so = ' '.join(lo)

print(so)
