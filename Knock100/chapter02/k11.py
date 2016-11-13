with open('hightemp.txt') as f:
    for s in f:
        print(s.replace('\t', ' ').strip())
