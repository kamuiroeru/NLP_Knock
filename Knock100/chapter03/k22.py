import k20
import re
from pprint import pprint

categories = re.findall('\[\[Category:.+\]\]', k20.read_jwc_json()['イギリス'])

cateWords = [re.sub('\]\]', '', word).split(':')[1] for word in categories]

pprint(cateWords)
# for cateWord in cateWords:
#     print(cateWord)
