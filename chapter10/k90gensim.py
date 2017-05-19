from gensim.models import word2vec
from os.path import exists

fname = 'gensim_word2vec_model.gensim'

if exists(fname):
    model = word2vec.Word2Vec.load(fname)
else:
    data = word2vec.Text8Corpus('../chapter09/out81.txt')
    model = word2vec.Word2Vec(data)
    model.save(fname)

def pos_neg(instr: str):
    positive = []
    negative = []
    templist = instr.rstrip().split(' ')
    if templist[-1] in '+-':
        print('Warning 行末の演算子は無視されます')
        templist.pop()
    while(templist):
        word = templist.pop()
        try:
            opr = templist.pop()
        except IndexError:
            opr = '+'
        if opr == '+':
            positive.append(word)
        else:
            negative.append(word)

    return positive, negative

def main(instr):
    pos, neg = pos_neg(instr)
    try:
        out = model.most_similar(topn=n, positive=pos, negative=neg)
    except KeyError as e:
        print('KeyError: ', e)
        return
    notifyStr = 'positive: {}, negative: {}'.format(' '.join(pos), ' '.join(neg))
    print(notifyStr)
    print(''.join(['=' for i in range(len(notifyStr))]))
    for x in out:
        print(x[0], '{:0.3f}'.format(x[1]))
    print()


n = 5
from sys import argv
if len(argv) == 2:
    n = int(argv[1])

import sys
import code
import readline
import atexit
import os

class MyConsole(code.InteractiveConsole):
    def __init__(self, local=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, local, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except IOError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.write_history_file(histfile)

    def push(self, line):
        main(line)


my_console = MyConsole()
sys.ps1 = ">> "
sys.ps2 = "------>> "
my_console.interact('### Lets word2vec ###')
