def cipher(input):
    l = []
    for s in input:
        a = int.from_bytes(s.encode(), 'big')
        if a >= 97 and a <= 122:
            a = 219 - a
        l.append(a.to_bytes(4, 'big').decode()[-1])
    return ''.join(l)


if __name__ == '__main__':
    s = 'I play soccer 3 times.'
    s1 = cipher(s)
    print(s1)
    s2 = cipher(s1)
    print(s2)
