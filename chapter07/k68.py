import k65

if __name__ == '__main__':
    col = k65.col
    query = {'tags.value': 'dance', 'rating': {'$exists': True}}
    top10 = {}
    for data in col.find(query):
        top10[data['name']] = data['rating']['count']
    top = sorted(top10.items(), key=lambda x: (-x[1], x[0]))[0:10]
    for lc, name in enumerate(top, start=1):
        print(lc, name[0])
