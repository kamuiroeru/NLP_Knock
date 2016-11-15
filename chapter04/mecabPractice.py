import MeCab

# m = MeCab.Tagger('-Ochasen')
m = MeCab.Tagger('mecabrc')
# mecabrcの場合の出力フォーマット
# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

while(True):
    print('>>>', end='')
    s = m.parse(str(input()))
    n = m.parseToNode(str(input()))
    print(s)
    print(n.surface + ','.join(n.feature))
