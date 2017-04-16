#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, url, get, post, response, error
import pymongo, re
from bson.objectid import ObjectId
from dictToHTML import convert

# グローバル変数
sorted_rank = []
total_count = 0
col = pymongo.MongoClient()['my']['nlp100']


@route('/')  # トップページ
def html_index():
    return template('index')


@route('/', method='POST')
def search():
    artist_name = request.forms.artist_name
    genre = request.forms.genre
    area = request.forms.area
    if artist_name or genre or area:
        return template(engine(artist_name, genre, area))
    else:
        return template('アーティスト名かジャンルを入力してください。<br><a href="/">戻る</a>')


# データベースを叩く
def engine(name: str, genre: str, area: str) -> str:
    forklist = [['name', name], ['genre', genre], ['area', area]]
    query = {}
    for s in forklist:  # 検索語句に応じて適切なクエリを作る
        if s[1]:
            if s[0] == 'name':
                query['$or'] = []
                query['$or'].append({'name': re.compile(name.rstrip(), re.IGNORECASE)})
                query['$or'].append({'aliases.name': re.compile(name.rstrip(), re.IGNORECASE)})
            elif s[0] == 'genre':
                query['tags.value'] = re.compile(genre.rstrip(), re.IGNORECASE)
            else:
                query['area'] = re.compile(area.rstrip(), re.IGNORECASE)

    global total_count, sorted_rank, col
    hit_data = col.find(query)
    total_count = hit_data.count()  # 検索個数をカウントして、
    print(total_count)
    if total_count > 100:  # 100件を超えてたら

        # レーティングされている項目だけで順位付けする。
        ranking = {data['_id']: data['rating']['count'] for data in hit_data if data.get('rating')}
        sorted_rank = sorted(ranking.items(), key=lambda x: x[1], reverse=True)  # レーティング数が多いもの順
        total_count = len(sorted_rank)  # 検索個数を修正
    # elif total_count == 1:
    #     idstr = hit_data.next()['_id']
    #     route('/details/' + str(idstr), )
        # details(str(idstr))
    else:
        sorted_rank = [(data['_id'], data['name']) for data in hit_data]  # そのまま吐き出す
    return show_part(0, sorted_rank)


# 10件ごとに情報を表示
def show_part(page: int, ranking: list) -> str:
    global total_count, col
    start = page * 10
    part_of_ranking = ranking[start:start + 10]  # rankingの一部
    html_string = str(total_count) + '件ヒット<br><a href="/">トップへ戻る</a>\n'
    html_string += '<br>{}~{}件を表示<br><ul>'.format(start, start + len(part_of_ranking))

    # リストでstart ~ start+10 個の名前とエリアを表示し、それぞれ詳細ページにリンクする。
    for idobj, count in part_of_ranking:
        in_dic = col.find_one({'_id': idobj})
        html_string += '<li><a href="{}" target="_blank">{}</a></li>\n' \
            .format('/details/' + str(in_dic['_id']), in_dic['name'] + ' : ' + str(in_dic.get('area') or ''))
    html_string += '</ul><br>'
    if not page == 0:  # 前ページにさらに10件以上あるとき
        html_string += '<a href="{}">前の10件</a>'.format('/page/' + str(page - 1))  # 前の10件ボタン追加
    if len(ranking[start:start + 11]) == 11:  # 後ページに1件以上あるとき、
        html_string += '   <a href="{}">次の10件</a>'.format('/page/' + str(page + 1))  # 次の10件ボタン追加
    return html_string


# 前・次の10件が押された時の処理
@route('/page/<num>')
def show_other_page(num: str):
    global sorted_rank
    return template(show_part(int(num), sorted_rank))


# 詳細ページを表示
@route('/details/<idstr>')
def details(idstr: str):
    global col

    # MongoDBの固有idであるidstrを使って目的の情報をGet
    detail_dic = col.find_one({'_id': ObjectId(idstr)})
    detail_dic.pop('_id')  # _idは要らないので除去
    html_str = convert(detail_dic)  # htmlを作る（dictToHTML.convertに投げる）
    html_str += '\n<br><hr><a href="#" onclick="window.close()">[閉じる]</a>\n</body>\n</html>'
    return template(html_str)


# @error(404)
# def error404(error):
#     return template("404")

@route('/hoge/<name>')
def hoge(name: str):
    huga = '<h1>pyo</h1>'
    return template('hoge', {'baka': huga})

import pickle

if __name__ == '__main__':

    # キャッシュファイルが無い時新規作成
    try:
        open('cache.pickle', 'rb')
    except FileNotFoundError:
        pickle.dump({}, open('cache.pickle', 'wb'))

    run(host="localhost", port=8000, debug=True, reloader=True)
