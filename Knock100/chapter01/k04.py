s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'.replace(
    ',', '').replace('.', '')
l = s.split(' ')
dic = {}
for w, r in zip(l, range(1, len(l))):
    if r in {1, 5, 6, 7, 8, 9, 15}:
        dic[w[:1]] = r
    else:
        dic[w[:2]] = r
print(dic)
