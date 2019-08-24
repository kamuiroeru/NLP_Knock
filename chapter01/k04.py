s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
s = s.replace(',', '').replace('.', '')
l = s.split(' ')
dic = {}
for lc, w in enumerate(l, start=1):
    if lc in {1, 5, 6, 7, 8, 9, 15}:
        dic[w[:1]] = lc
    else:
        dic[w[:2]] = lc
print(dic)
