# ストップワードリストが複数入った辞書を作る
def load_stop_words(fname: str, encode='utf-8') -> dict:
    import json
    if fname.split('.')[-1] == 'gz':
        import gzip
        jstring = gzip.open(fname, 'rb').read().decode()
    else:
        jstring = open(fname).read()

    return json.loads(jstring, encoding=encode)


stopWordDict = load_stop_words('stopWords/JsonStopWordlist.json.gz')

# 使用するストップワードリストを集合に
stSet = set(stopWordDict['RANKSNL_Default'])


def in_swlist(string: str) -> bool:
    return True if string in stSet else False  # 3項演算子


if __name__ == '__main__':
    from sys import argv

    if len(argv) < 3:
        print('引数が足りません')
        exit(0)
    else:
        strList = argv[2:]
        for string in strList:
            print(string, in_swlist(string))
