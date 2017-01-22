import requests, json, threading
from bs4 import BeautifulSoup
from time import sleep

url = ''


def getpic(name: str) -> None:
    global url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    payload = {'q': name, 'tbm': 'isch', 'tbs': 'itp:face'}
    r = requests.get('https://www.google.co.jp/search?', headers=headers, params=payload)
    while r.status_code != 200:
        sleep(1)
        r = requests.get('https://www.google.co.jp/search?', headers=headers, params=payload)

    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.select('div .rg_meta')[0]
    url = json.loads(str(data.contents[0]))['ou']


def convert(d: dict) -> str:
    name = d['name']
    thread1 = threading.Thread(target=getpic, args=(name,))
    thread1.start()
    ret_str = '''<!DOCTYPE html>
                <html lang="ja">
                <head>
                <meta charset="UTF-8">
                <title>{}</title>
                </head>
                <body>\n'''.format(d['name'])

    ret_str += '<h1>{}</h1>\n'.format(d['name'])
    ret_str += '<table border="0"><tr><td>'

    def hoge(lis: list) -> None:
        nonlocal ret_str
        ret_str += '<table border="1">\n'
        for elem in lis:
            key, val = elem[0], elem[1]
            ret_str += '<tr><td>{}</td><td>'.format(key)
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

    thread1.join()
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
