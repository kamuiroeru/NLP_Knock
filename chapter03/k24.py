import k20
import re
from pprint import pprint

# Windowsのファイル名禁止文字「\ / : * < > |」以外 が 1個以上 .(ピリオド）が1個 英字4個まで」の文字列を取ってくる。
sections = re.findall(':[^\\\/:\*\?\"\<\>\|]+\.[a-zA-Z]{,4}\|', k20.read_jwc_json()['イギリス'])

pprint(sections)
