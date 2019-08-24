# coding: utf-8

# 全文読み込み
instr = open('./questions-words.txt').read()

# セクションで区切ってから改行で区切る
sections = [section.split('\n') for section in instr.split(':')]

# セクションごとに辞書にまとめる
sectionsDic = {l[0].strip(): l[1:] for l in sections}

# 書き込み
open('out91.txt', 'w').write('\n'.join(sectionsDic['family']))
