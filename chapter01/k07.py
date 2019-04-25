def ret_char(x=10, y='おやつのポン・デ・リング', z='神'):
    return '{}時の{}は{}'.format(x, y, z)
    # 3.6 以降なら return f'{x}時の{y}は{z}' でOK


if __name__ == '__main__':
    print(ret_char(12, '気温', 22.4))
    print(ret_char())
