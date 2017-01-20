from collections import defaultdict
from pprint import pprint

import k65

if __name__ == '__main__':
    col = k65.col
    query = {'tags.value': 'dance', 'rating': {'$exists': True}}
    top10 = {}
    for data in col.find(query):
        top10[data['name']] = data['rating']['count']
    pprint(sorted(top10.items(), key=lambda x: x[1], reverse=True)[0:10])
