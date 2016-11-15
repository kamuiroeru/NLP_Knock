s = 'stressed'
l = len(s)
ns = ''.join([s[l - 1 - x: l - x] for x in range(len(s))])
print(ns)

print(s[::-1])