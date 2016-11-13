import k20
from pprint import pprint

s = str(k20.read_jwc_json()['イギリス'])
lines = s.split()

# categories = []
# for line in lines:
#     if 'Category' in line:
#         categories.append(line)
categories = [line for line in lines if 'Category' in line]

pprint(categories)
# for category in categories:
#     print(category)
