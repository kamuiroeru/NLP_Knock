def convert(d: dict) -> str:
    # global ret_str
    ret_str = '''<!DOCTYPE html>
                <html lang="ja">
                <head>
                <meta charset="UTF-8">
                <title>{}</title>
                </head>
                <body>\n'''.format(d['name'])

    ret_str += '<h1>{}</h1>\n'.format(d['name'])

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
    return ret_str


if __name__ == '__main__':
    print()
