with open('nlp50.out') as f:
    for line in f:
        if line.rstrip():
            for word in line.split(' '):
                print(word.rstrip())
        print()
