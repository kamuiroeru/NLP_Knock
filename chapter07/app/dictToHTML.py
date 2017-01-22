import requests, json, threading, pickle
from bs4 import BeautifulSoup
from time import sleep
import time

url = ''


# google画像検索結果のトップの画像を表示させる。
def getpic(name: str, type: str) -> None:
    global url
    cache = pickle.load(open('cache.pickle', 'rb'))
    url = cache.get(name)
    if not url:
        # ヘッダ情報（これがないと、画像のURLもらえない）
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        if type == 'Person':  # タイプが人の時、検索種類を「顔」に
            payload = {'q': name, 'tbm': 'isch', 'tbs': 'itp:face'}
        else:  # それ以外、検索種類を「写真」に
            payload = {'q': name, 'tbm': 'isch', 'tbs': 'itp:photo'}

        st = time.time()
        r = requests.get('https://www.google.co.jp/search?', headers=headers, params=payload)
        retry = 0
        while r.status_code != 200 and retry < 3:  # 正常に取得できなければ、3回までやり直す
            sleep(1)
            r = requests.get('https://www.google.co.jp/search?', headers=headers, params=payload)
            retry += 1
        print(time.time() - st)

        st = time.time()
        s = r.content.decode().split('</head>')[1]  # </head>までの情報が多すぎてsoupの作成に時間がかかるのでカット
        print(time.time() - st)

        st = time.time()
        soup = BeautifulSoup(s, 'html.parser')
        print(time.time() - st)

        st = time.time()
        data = soup.select('div .rg_meta')[0]  # 画像の詳細が詰まったリストの先頭
        print(time.time() - st)

        st = time.time()
        url = json.loads(str(data.contents[0]))['ou']  # 画像の元データURL
        print(time.time() - st)

        st = time.time()
        cache[name] = url
        pickle.dump(cache, open('cache.pickle', 'wb'))
        print(time.time() - st)


def convert(d: dict) -> str:
    name = d['name']

    # マルチスレッド開始
    thread1 = threading.Thread(target=getpic, args=(name, d.get('type') or 'Unknown'))
    thread1.start()

    st = time.time()
    ret_str = '''<!DOCTYPE html>
                <html lang="ja">
                <head>
                <meta charset="UTF-8">
                <title>{}</title>
                </head>
                <body>\n'''.format(d['name'])

    ret_str += '<h1>{}</h1>\n'.format(d['name'])
    ret_str += '<table border="0">\n<tr><td>'

    # dict -> html tableにする関数（このデータ専用）
    def hoge(lis: list) -> None:
        nonlocal ret_str
        ret_str += '\n<table border="1">\n'
        for elem in lis:
            key, val = elem[0], elem[1]
            ret_str += '\n<tr><td>{}</td><td>'.format(key)
            if key == 'tags':
                inval = []
                for data in val:
                    temp = list(data.values())
                    if isinstance(temp[0], int):
                        temp.reverse()
                    inval.append(tuple(temp))
                inval = sorted(inval, key=lambda x: x[1], reverse=True)
                hoge(inval)
            elif key == 'aliases':
                inval = []
                for data in val:
                    for k, v in data.items():
                        if k == 'name':
                            inval.append((k, v))
                hoge(inval)
            elif isinstance(val, list) or isinstance(val, dict):
                if 'items' in dir(val):
                    val = [(k, v) for k, v in val.items()]
                else:
                    val = [(k, v) for k, v in val]
                hoge(val)
            else:
                ret_str += str(val)
            ret_str += '</td></tr>'
        ret_str += '\n</table>'

    d = [(k, v) for k, v in d.items()]
    hoge(d)
    print('main: ' + str(time.time() - st))

    thread1.join()  # 写真のURLが取れるのを待つ
    global url
    ret_str += '''</td>
        <td valign="top">
            <a href="{}">
                <img src="{}" alt="{}" title="{}" height="150">
            </a>
        </td>
    </tr>
    </table>'''.format(url, url, name, name)
    return ret_str


if __name__ == '__main__':
    print()
