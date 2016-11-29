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

data = pd.DataFrame({'出現頻度': [l[1] / total for l in sorted_list]})

print(data)
sns.set_style('whitegrid') #軸設定とかよりも前に指定
# sns.plt.xlim([0, 0.0006])
# sns.plt.ylim([0, 2000])
sns.plt.xlabel('出現頻度')
sns.plt.ylabel('単語の個数')
sns.set_context("notebook", 1.3)  # 文字の大きさ変更
# sns.distplot(data['出現頻度'], kde=False, bins=14, color='red', hist_kws={"alpha": 1, 'normed': True})
n, bins, patches = sns.plt.hist(data['出現頻度'], bins=14, color='blue')
patches[0].set_facecolor('orangered')
sns.set_palette("hot", 10)  # 色変更
sns.plt.title('ヒストグラム')
sns.plt.show()
