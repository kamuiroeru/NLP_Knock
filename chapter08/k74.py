from k72 import remove_waste
from k73 import sigmoid
import pickle

dic = pickle.load(open('model.pkl', 'rb'))


def likelihood(inputobj: {str, list, tuple}) -> tuple:
    """リストかスペース区切りのstrを読み込んで、(正解極性ラベル, 予測確率)のタプルを返す。"""

    numofsum = 0.0  # 重みの合計

    #  入力がstrだった時の処理
    if isinstance(inputobj, str):
        inputobj = inputobj.split(' ')

    for word in inputobj[1:]:
        numofsum += dic[word]
    return inputobj[0], sigmoid(numofsum)


if __name__ == '__main__':
    from sys import argv
    from subprocess import getoutput
    from argparse import ArgumentParser

    parse = ArgumentParser()
    parse.add_argument('--input', '-i', help='input filename', default='sentiment.txt')
    parse.add_argument('--num', '-n', help='line number', default=1, type=int)
    parse.add_argument('--raw', '-r', help='use raw string', default=False, action='store_true')
    args = parse.parse_args()

    instr = ''
    try:
        if args.raw:
            instr = argv[-1]
            if instr == '-r':
                raise IndexError
        else:
            instr = getoutput('head -n{} {}|tail -n1'.format(args.num, args.input))
    except IndexError:
        print('入力がありません。')
        exit(1)

    inlist = instr.split(' ')

    print('input: "{}"\n'.format(instr))
    print('words: {}\n'.format(remove_waste(inlist[1:])))
    print('ans:', *likelihood(inlist + remove_waste(inlist[1:])))
