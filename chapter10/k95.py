import pandas as pd

df = pd.read_csv('out94.csv')
del df['Unnamed: 0']

def ranking(colmunName):
    rank = df.sort_values(by=[colmunName], ascending=False)  # ascending=Falseで降順、Trueなら昇順
    rank = rank.reset_index(drop=True)  # 連番振り直し
    return pd.concat([rank['Word 1'], rank['Word 2'], rank[colmunName]], axis=1)  # 右から結合


rankHuman = ranking('Human (mean)')
rankGensim = ranking('gensim')
rankMysystem = ranking('mysystem')

print(rankHuman)
print(rankGensim)
print(rankMysystem)

# (スピアマン)相関係数を求めるpandasの関数
cor = df.corr()

print('Human Gensim: {0:0.3f}'.format(cor['Human (mean)']['gensim']))
print('Human Mysystem: {0:0.3f}'.format(cor['Human (mean)']['mysystem']))
