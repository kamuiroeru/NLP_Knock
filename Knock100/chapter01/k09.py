import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
lo = []
for i in s.split(' '):
    if len(i) > 4:
        temp = []
        l = list(i)
        lo.append(l[0] + ''.join([l.pop(random.randint(1, len(l) - 1)) for none in range(1, len(l) - 1)]) + l[-1])
        # temp.append(l[0])
        # for none in range(1, len(l) - 1):
        #     temp.append(l.pop(random.randint(1, len(l) - 1)))
        # temp.append(l[-1])
        # lo.append(''.join(temp))
    else:
        lo.append(i)
so = ' '.join(lo)

print(so)
