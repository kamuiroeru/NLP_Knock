import json
from collections import Counter
from operator import itemgetter
import pandas as pd
import seaborn as sns

with open('out.json') as fi:
    sentence = json.load(fi)
    total = len(sentence)
    sorted_list = sorted(Counter([morpheme['base'] for morpheme in sentence]).most_common(), key=itemgetter(1, 0),
                         reverse=True)

data = pd.DataFrame({'品詞': [l[0] for l in sorted_list],
                     '出現頻度': [l[1] / total for l in sorted_list]})
sns.plt.xlim([0, 0.0006])
sns.plt.ylim([0, 100])
sns.set_context("notebook", 1.3)  # 文字の大きさ変更
# sns.set_palette("hot", 10)  # 色変更
sns.distplot([l[1] / total for l in sorted_list], kde=False, rug=True, bins=4000)
sns.plt.title('ヒストグラム')
sns.plt.show()
