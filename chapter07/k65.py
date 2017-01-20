import pymongo

client = pymongo.MongoClient()
db = client['my']  # データベース名 補完が効くのでこちらの書き方がおすすめ
col = db['nlp100']  # コレクション名

if __name__ == '__main__':
    query = {'name': 'Queen'}
    for data in col.find(query):
        print(data)
