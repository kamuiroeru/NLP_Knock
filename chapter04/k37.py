import json
from collections import Counter
from operator import itemgetter
import pandas as pd
import seaborn as sns

with open('out.json') as fi:
    sentence = json.load(fi)
    total = len(sentence)
    sorted_list_top10 = sorted(Counter([morpheme['base'] for morpheme in sentence]).most_common(), key=itemgetter(1, 0),
                               reverse=True)[:10]

data = pd.DataFrame({'単語': [l[0] for l in sorted_list_top10],
                     '出現頻度': [l[1] / total for l in sorted_list_top10]})
# sns.plt.ylim([0, 0.1]) #y軸の最大値設定
sns.set_context("notebook", 1.3)  # 文字の大きさ変更
sns.set_palette("winter", 10)  # 色変更
sns.barplot(x='単語', y='出現頻度', data=data)
sns.plt.title('頻出Top10')
sns.plt.show()
