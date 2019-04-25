from k05 import n_gram  # k05.pyのn_gramを導入

s1 = 'paraparaparadise'
s2 = 'paragraph'

X = set(n_gram(s1, 2) + [''])
Y = set(n_gram(s2, 2) + [''])
judge1 = 'se' in X
judge2 = 'se' in Y

union = X | Y
pro_set = X & Y
diff_set = X - Y

print('X ∪ Y：' + str(union))
print('X ∩ Y：' + str(pro_set))
print('X - Y：' + str(diff_set))
print('Xに\'se\'は含まれるか: ' + str(judge1))
print('Yに\'se\'は含まれるか: ' + str(judge2))
