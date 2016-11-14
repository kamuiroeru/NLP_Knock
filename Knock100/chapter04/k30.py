import MeCab

m = MeCab.Tagger('-Ochasen')

fi = open('neko.txt')
fo = open('nekoMecab.txt', 'a')

with fi, fo:
    for line in fi.readlines():
        print(m.parse(line.strip()), file=fo)