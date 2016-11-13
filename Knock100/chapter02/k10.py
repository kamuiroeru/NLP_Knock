# with open('hightemp.txt', 'r', encoding='utf-8') as f:
#     while(True):
#         s = f.readline();

num_lines = sum([1 for line in open('hightemp.txt')])
print(num_lines)
