with open('nlp50.out') as f:
    for line in f:
        for word in line.split(' '):
            print(word)
