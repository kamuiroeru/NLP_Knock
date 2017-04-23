import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from k77 import ret_score


def classify_neo(ans, odds, border) -> str:
    """正解と予測確率としきい値を与えると、TP, FP, TN, FNのいずれかを返す"""

    odds = float(odds)
    if odds >= border:
        return 'TP' if int(ans) > 0 else 'FP'
    else:
        return 'TN' if int(ans) < 0 else 'FN'


sns.set_style('whitegrid')
sns.set_context('talk', 1.5, {"lines.linewidth": 5})

resolution = 10

indf = pd.read_table('k76output.txt', header=None)
indf.columns = ['ans', 'prediction', 'odds']
print(indf)

x = np.arange(0, 1, 1 / resolution)
accuracys, precisions, recalls, F_measures = np.zeros(len(x) * 4).reshape(4, len(x))

for lc, border in enumerate(x):
    print('calculating: border ' + str(border))
    tempdic = {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}
    for key, obj in indf.iterrows():
        tempdic[classify_neo(obj['ans'], obj['odds'], border)] += 1

    accuracys[lc], precisions[lc], recalls[lc], F_measures[lc] = \
        ret_score(*map(lambda label: tempdic[label], ['TP', 'FP', 'TN', 'FN']))

p1 = plt.plot(x, precisions)
p2 = plt.plot(x, recalls)
# p3 = plt.plot(x, accuracys)
# p4 = plt.plot(x, F_measures)
# plt.legend((p1[0], p2[0], p3[0], p4[0]), ('presicion', 'recall', 'accuracy', 'F_measure'), loc='best')
plt.legend((p1[0], p2[0]), ('presicion', 'recall'), loc='best')
plt.show()
