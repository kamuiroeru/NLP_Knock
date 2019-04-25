def n_gram(s, n):
    if n == 0:
        print('Can\'t make 0-gram')
        return None
    else:
        end = len(s) - n + 1
        i = 0
        l = []
        while i < end:
            l.append(s[i:i + n])
            i += 1
        return l


if __name__ == '__main__':
    print(n_gram('I am an NLPer.'.split(' '), 2))  # 単語bi-gram
    print(n_gram('I am an NLPer.', 2))  # 文字bi-gram
