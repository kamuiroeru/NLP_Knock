import k20
import re
from pprint import pprint

# 「=が2個以上 .(なんか文字）が1個以上 =が2個以上」の文字列を取ってくる。
sections = re.findall('={2,}.+={2,}', k20.read_jwc_json()['イギリス'])

pprint(sections)
section_and_level = {''.join(re.findall('[^=]+', section)).strip(): int(len(re.findall('=', section))/2 - 1)
                     for section in sections
                     }

pprint(section_and_level)
# for sec, level in section_and_level.items():
#     print('N : {0:<10}, L : {1}'.format(sec, level))
