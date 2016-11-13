s1 = 'パトカー'
s2 = 'タクシー'
ns = ''
for x, y in zip(s1, s2):
    ns += x + y
# ns = ''.join([s[x:x + 1] for x in range(len(s)) if x % 2 == 1])
print(ns)
