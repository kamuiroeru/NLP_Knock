import json
from collections import Counter
from operator import itemgetter
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open('out.json') as fi:
    sentence = json.load(fi)
    total = len(sentence)
    sorted_list = sorted(Counter([morpheme['base'] for morpheme in sentence]).most_common(), key=itemgetter(1, 0),
                         reverse=True)

data = pd.DataFrame({'出現頻度': [l[1] / total for l in sorted_list],
                     '順位': [i for i in range(len(sorted_list))]})
sns.set_context("notebook", 1.3)  # 文字の大きさ変更
# sns.set_palette("hot")  # 色変更
plt.xscale('log')
plt.yscale('log')
plt.xlabel('順位')
plt.ylabel('出現頻度')
plt.plot('順位', '出現頻度', data=data)
plt.title('ヒストグラム')
plt.show()
