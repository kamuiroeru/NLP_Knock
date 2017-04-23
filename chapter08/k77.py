def classify(instr: str) -> str:
    """
        '正解\t予測\t予測確率'の文字列から、
        TP: 予測が的中してPositive
        TN: 予測が的中してNegative
        FP: 予測が外れてPositive
        FN: 予測が外れてNegative
        のいずれかを返す
    """

    ans, prediction, odds = instr.split('\t')
    if ans == '+1':
        return 'TP' if prediction == '+1' else 'FP'
    else:
        return 'TN' if prediction == '-1' else 'FN'


def ret_score(TP, FP, TN, FN) -> tuple:
    """TP, FP, TN, FNを渡すと、正解率, 適合率, 再現率, F1スコアをタプルで返す関数"""

    rate_of_correct_ans = (TP + TN) / (TP + FP + TN + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F_measure = 2 * precision * recall / (precision + recall)

    return rate_of_correct_ans, precision, recall, F_measure


if __name__ == '__main__':
    from collections import Counter

    classified = Counter([classify(line.rstrip()) for line in open('k76output.txt')])
    TP, FP, TN, FN = map(lambda x: classified[x], ['TP', 'FP', 'TN', 'FN'])

    rate_of_correct_ans, precision, recall, F_measure = ret_score(TP, FP, TN, FN)

    print('正解率:\t{}'.format(rate_of_correct_ans))
    print('適合率:\t{}'.format(precision))
    print('再現率:\t{}'.format(recall))
    print('F1スコア:\t{}'.format(F_measure))
