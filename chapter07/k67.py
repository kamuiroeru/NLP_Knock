from pprint import pprint

import k65

if __name__ == '__main__':
    col = k65.col
    while True:
        s = ''
        try:
            s = input('>>>')
        except KeyboardInterrupt:
            exit(0)
        # for data in col.find({'name': s}):
        #     print(data)
        for data in col.find({'aliases.name': s}, {'_id': 0}):
            pprint(data)
