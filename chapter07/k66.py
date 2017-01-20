# MongoDBのインタラクティブシェルでは
# find({"area":"Japan"}).count()
# を実行する

import k65

if __name__ == '__main__':
    query = {"area": "Japan"}
    print(k65.col.count(query))
