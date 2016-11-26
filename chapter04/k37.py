import json
from collections import Counter

# from resource import getrusage,RUSAGE_SELF
from operator import itemgetter

import pandas as pd
import seaborn as sns

with open('out.json') as fi:
    # print(getrusage(RUSAGE_SELF).ru_maxrss)
    sentence = json.load(fi)
    total = len(sentence)
    sorted_list = sorted(Counter([morpheme['base'] for morpheme in sentence]).most_common(), key=itemgetter(1, 0),
                         reverse=True)[:10]
    # for word, count in sorted_list:
    #     print(word, count / total)
    # print(word)
    # print(getrusage(RUSAGE_SELF).ru_maxrss)

data = pd.DataFrame({'品詞': [l[0] for l in sorted_list],
                     '出現頻度': [l[1] / total for l in sorted_list]})
# sns.plt.ylim([0, 0.1])
sns.set_context("notebook", 1.3)
sns.set_palette("hot", 10)
sns.barplot(x='品詞', y='出現頻度', data=data)
sns.plt.title('頻出Top10')
sns.plt.show()
