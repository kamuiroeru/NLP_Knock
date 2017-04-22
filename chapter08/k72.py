import re
from nltk import stem
import k71


def remove_waste(instr) -> list:
    """単語に分けて、記号やストップワードを除去したあと、ステミングする。
"""

    return_list = []
    st = stem.PorterStemmer()
    templist = []
    if isinstance(instr, str):
        templist = instr.split(' ')
    else:
        templist = instr

    for word in templist:
        word_for_stem = re.sub("[^0-9a-z']", '', word.lower())
        if word_for_stem:  # 記号のみを除去
            if not k71.in_swlist(word_for_stem):  # ストップワードなら除去
                return_list.append(st.stem(word_for_stem))

    return return_list


from collections import Counter, defaultdict


def tf(in_list: list) -> dict:
    """単語(str)が入ったリストを入力にとり、tf(dict)を返す"""

    temp_dict = dict(Counter(in_list))
    return {k: v / len(in_list) for k, v in temp_dict.items()}


from math import log


def idf(word: str, document_dicts: list) -> float:
    """単語と全文書のtf(dictまたはset)が入ったリストを引数にとり、単語のidf(float)を返す。"""

    df = Counter([True for dic in document_dicts if word in dic])[True]
    n = len(document_dicts)

    return log(n / df) + 1


def dump_tfidf():
    from time import time
    start = time()

    # それぞれの文における各単語のtfとposnegを保存
    tfList = []
    posnegList = []
    for line in open('sentiment.txt'):
        lineSplit = line.rstrip().split(' ')
        posnegList.append(lineSplit[0])
        tfList.append(tf(remove_waste(lineSplit[1:])))
    print('posneg, tf List complete : {} [sec]'.format(time() - start))

    # それぞれの文における各単語のtfidfを保存
    idfList = []
    tfidfList = []
    for dic in tfList:
        indic = {}
        for word, tfVal in dic.items():
            thisIdf = idf(word, tfList)
            indic[word] = tfVal * thisIdf
        tfidfList.append(indic)
    print('tfidf List complete : {} [sec]'.format(time() - start))

    # posな文におけるtfidfの順位と、negにおける(ryを見つける
    # 異なる文におけるtfidfは違うので、pos neg それぞれで単語ごとにまとめる
    pos, neg = defaultdict(list), defaultdict(list)
    for posneg, dic in zip(posnegList, tfidfList):
        for word, tfidf in dic.items():
            if posneg == '+1':
                pos[word].append(tfidf)
            else:
                neg[word].append(tfidf)
    print('posneg marge complete : {} [sec]'.format(time() - start))

    posList = sorted([(word, sum(tfidfs) / len(tfidfs)) for word, tfidfs in pos.items()]
                     , key=lambda x: x[1], reverse=True)
    negList = sorted([(word, sum(tfidfs) / len(tfidfs)) for word, tfidfs in neg.items()]
                     , key=lambda x: x[1], reverse=True)

    print(posList[:5])
    print(negList[:5])

    import pickle

    pickle.dump(posnegList, open('posnegList.pkl', 'wb'))
    pickle.dump(tfList, open('tfList.pkl', 'wb'))
    pickle.dump(posList, open('posList.pkl', 'wb'))
    pickle.dump(negList, open('negList.pkl', 'wb'))

    print('posneg rankup compete : {} [sec]'.format(time() - start))

if __name__ == '__main__':
    dump_tfidf()