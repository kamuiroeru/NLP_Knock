from pprint import pprint
import re

import k65

if __name__ == '__main__':
    col = k65.col
    while True:
        s = ''
        try:
            s = input('>>>')
        except KeyboardInterrupt:
            exit(0)
        print(s)
        for data in col.find({'aliases.name': re.compile(s, re.IGNORECASE)}, {'_id': 0}):  # _idが出てくると鬱陶しいので除外
            pprint(data)
