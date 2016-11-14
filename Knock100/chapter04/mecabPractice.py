import MeCab

m = MeCab.Tagger('-Ochasen')

while(True):
    print('>>>', end='')
    s = m.parse(str(input()))
    print(s)
