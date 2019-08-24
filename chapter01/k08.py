def cipher(strin):
    char_list = []
    for char in strin:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_list.append(chr(219 - char_code))
        else:
            char_list.append(chr(char_code))
    return ''.join(char_list)
#

if __name__ == '__main__':
    s = 'I play soccer 3 times.'
    s1 = cipher(s)
    print(s1)
    s2 = cipher(s1)
    print(s2)
