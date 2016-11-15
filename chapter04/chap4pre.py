import MeCab

m = MeCab.Tagger('mecabrc')

fi = open('neko.txt')
fo = open('neko.txt.mecab', 'w')

with fi, fo:
    s = ''
    for line in fi.readlines():
        s += m.parse(line.strip())
    fo.write(s)
