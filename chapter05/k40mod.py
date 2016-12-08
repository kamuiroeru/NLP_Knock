from makePickle import pickleLoad

lines = pickleLoad('out.pickle')
for l in lines[2]:
    print(l.surface, l.base, l.pos, l.pos1)
