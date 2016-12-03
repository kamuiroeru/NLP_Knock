import makePickle as mp
from k40 import create_morph

mp.pickleDump(create_morph(), 'out')
dic = mp.pickleLoad('out.pickle')
print(list(map(lambda x: x.surface, dic[2])))
