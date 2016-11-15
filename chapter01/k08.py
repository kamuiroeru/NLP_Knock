def cipher(strin):
    l = []
    for word in strin:
        a = int.from_bytes(word.encode(), 'big')
        if 97 <= a <= 122:
            a = 219 - a
        l.append(a.to_bytes(4, 'big').decode()[-1])
    return ''.join(l)

    # もっとかんたんなやり方あります
    # text_list = [chr(219 - ord(char)) if char.islower() else char for char in strin]
    # return ''.join(text_list)


if __name__ == '__main__':
    s = 'I play soccer 3 times.'
    s1 = cipher(s)
    print(s1)
    s2 = cipher(s1)
    print(s2)
