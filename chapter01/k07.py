def ret_char(x=10, y='おやつのポン・デ・リング', z='神'):
    return ('{0}時の{1}は{2}'.format(x, y, z))


if __name__ == '__main__':
    print(ret_char(12, '気温', 22.4))
    print(ret_char())
