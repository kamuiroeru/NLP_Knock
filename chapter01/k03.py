s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
s = s.replace(',','').replace('.','')
l = [len(x) for x in s.split(' ')]
print(l)
