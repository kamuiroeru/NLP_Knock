from pprint import pprint
import k28
import requests
from urllib import parse

url = 'http://ja.wikipedia.org/w/api.php?format=json&action=query&prop=imageinfo&titles={}&iiprop=url'.format(
    parse.quote('ファイル:' + k28.parse_wiki()['国旗画像']))

resp = requests.get(url).json()
a = resp['query']['pages']['-1']['imageinfo'][0]['url']
print(a)
pprint(resp)
