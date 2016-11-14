import MeCab

m = MeCab.Tagger('-Ochasen')

with open('neko.txt.mecab') as fi:
    for line in fi.readlines():
