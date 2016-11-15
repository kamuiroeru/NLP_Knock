import k20
import re
from pprint import pprint

# findall(pattern, string) : stringからpatternにマッチする部分文字列を全て探し出しlistとして返す。
categories = re.findall('\[\[Category:.+\]\]', k20.read_jwc_json()['イギリス'])

# もっと理解しやすい方法で書くと、
# p = re.compile('\[\[Category:.+\]\]')
# categories = p.findall(k20.read_jwc_json()['イギリス'])

pprint(categories)
# for category in categories:
#     print(category)
