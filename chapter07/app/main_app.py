#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, url, get, post, response, error
import pymongo, re
from bson.objectid import ObjectId

sorted_rank = []
total_count = 0
col = pymongo.MongoClient()['my']['nlp100']


@route('/')
def html_index():
    return template('index')


@route('/page/<num>')
def show_other_page(num: str):
    global sorted_rank
    return template(show_part(int(num), sorted_rank))


def show_part(start: int, ranking: list) -> str:
    global total_count, col
    start *= 10
    html_string = str(total_count) + '件ヒット<br><a href="/">トップへ戻る</a>\n'
    html_string += '<br>{}~{}件を表示<br><ul>'.format(start, start + 10)
    col = pymongo.MongoClient()['my']['nlp100']
    for id, count in ranking[start:start + 10]:
        in_dic = col.find_one({'_id': id})
        html_string += '<li><a href="{}" target="_blank">{}</a></li>' \
            .format('/details/' + str(in_dic['_id']), in_dic['name'] + ' : ' + str(in_dic.get('area') or ''))
    html_string += '</ul><br>'
    start //= 10
    if not start == 0:
        html_string += '<a href="{}">前の10件</a>'.format('/page/' + str(start - 1))
    if len(ranking[start:start + 11]) == 11:
        html_string += '   <a href="{}">次の10件</a>'.format('/page/' + str(start + 1))
    return html_string


def engine(name: str, genre: str, area: str) -> str:
    # var_name = lambda val: [k for k, v in globals().items() if id(v) == id(val)]  # 変数名取得する関数
    forklist = [['name', name], ['genre', genre], ['area', area]]
    forklist = [e for e in forklist if e[1]]
    if len(forklist) > 1:
        query = {'%or': []}
        for s in forklist:
            if s[0] == 'name':
                query['$or'].append({'name': re.compile(name.rstrip(), re.IGNORECASE)})
                query['$or'].append({'aliases.name': re.compile(name.rstrip(), re.IGNORECASE)})
            elif s[0] == 'genre':
                query['$or'].append({'tags.value': re.compile(genre.rstrip(), re.IGNORECASE)})
            else:
                query['$or'].append({'area': re.compile(area.rstrip(), re.IGNORECASE)})
    else:
        query = {forklist[0][0]: re.compile(forklist[0][1].rstrip(), re.IGNORECASE)}
    global total_count, sorted_rank, col
    total_count = col.count(query)
    print(total_count)
    if total_count > 50:
        query['rating.count'] = {'$exists': True}
        ranking = {data['_id']: data['rating']['count'] for data in col.find(query)}
        sorted_rank = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
        total_count = len(sorted_rank)
        return show_part(0, sorted_rank)
    else:
        sorted_rank = [(data['_id'], data['name']) for data in col.find(query)]
        return show_part(0, sorted_rank)


from dictToHTML import convert


@route('/details/<idstr>')
def details(idstr: str):
    global col
    detail_dic = col.find_one({'_id': ObjectId(idstr)})
    detail_dic.pop('_id')
    html_str = convert(detail_dic)
    html_str += '\n<br><hr><a href="#" onclick="window.close()">[閉じる]</a>\n</body>\n</html>'
    return template(html_str)


@route('/', method='POST')
def search():
    artist_name = request.forms.artist_name
    genre = request.forms.genre
    area = request.forms.area
    if artist_name or genre or area:
        return template(engine(artist_name, genre, area))
    else:
        return template('アーティスト名かジャンルを入力してください。<br><a href="/">戻る</a>')


# @error(404)
# def error404(error):
#     return template("404")


if __name__ == '__main__':
    run(host="localhost", port=8000, debug=True, reloader=True)
