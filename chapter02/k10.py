# with open('hightemp.txt', 'r', encoding='utf-8') as f:
#     while(True):
#         s = f.readline();

from sys import argv

num_lines = sum([1 for line in open(argv[1])])
print(num_lines)
