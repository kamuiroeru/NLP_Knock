s = 'パタトクカシーー'
# l = []
# for x in range(len(s)):
#     if x % 2 == 1:
#         l.append(s[x:x+1])
# ns = ''.join(l)
ns = ''.join([s[x:x+1] for x in range(len(s)) if x % 2 == 1])
print(ns)

print(s[1::2])