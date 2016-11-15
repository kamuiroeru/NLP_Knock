def ngram(self='NoString', n=1):
    if n == 0:
        print('Can\'t make 0-gram')
        return None
    else:
        end = len(self) - n + 1
        i = 0
        l = []
        while i < end:
            l.append(self[i:i + n])
            i += 1
        return l


if __name__ == '__main__':
    print(ngram('I am an NLPer.', 2))
