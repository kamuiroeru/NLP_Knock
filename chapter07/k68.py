import k65

if __name__ == '__main__':
    col = k65.col
    query = {'tags.value': 'dance', 'rating': {'$exists': True}}
    top = {}
    for data in col.find(query):
        top[data['name']] = data['rating']['count']

    # レーティング数で降順ソート & nameを辞書昇順ソート
    top10 = sorted(top.items(), key=lambda x: (-x[1], x[0]))[0:10]
    for lc, name in enumerate(top10, start=1):
        print(lc, name[0])
