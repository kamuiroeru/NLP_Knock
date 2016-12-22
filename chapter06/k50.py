import re

with open('nlp.txt') as f:
    for l in f:
        line = l.rstrip()
        if line:
            finditer = re.finditer('(\.|;|:|\?|!){1} [A-Z]', line)  # 終端記号+スペース+大文字
            top = 0
            for match in finditer:
                print(line[top:match.start() + 1])  # 終端記号まで取る
                top = match.end() - 1  # 大文字は除去しない
