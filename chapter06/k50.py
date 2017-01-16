import re

with open('nlp.txt') as f:
    sentence = ''
    for line in f:
        findlist = list(re.finditer(r'[.;:?!] [A-Z]', line))  # 終端記号+スペース+大文字
        if findlist:
            top = 0
            for match in findlist:
                sentence += line[top:match.start() + 1]
                print(sentence)  # 終端記号まで取る
                top = match.end() - 1  # 大文字は除去しない
                sentence = ''
            print(line[top:-1])
        else:
            sentence += line
    print(sentence, end='')
