from k74 import dic
from pprint import pprint

dic_sorted = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

heavy = dic_sorted[:10]
light = dic_sorted[-10:]

print('重みの高い素性トップ10')
pprint(heavy)

print('重みの低い素性トップ10')
pprint(list(reversed(light)))
