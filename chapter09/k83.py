from collections import defaultdict
import numpy as np

dic_word_context_count = defaultdict(int)
dic_word_count = defaultdict(int)
dic_context_count = defaultdict(int)

for lc, line in enumerate(open('out82.tsv')):
    if lc % 100000 == 0:
        print('lc: ' + str(lc))
    line = line.rstrip().split()
    t = line[0]
    for c in line[1:]:
        dic_word_context_count[(t, c)] += 1
        dic_word_count[t] += 1
        dic_context_count[c] += 1

    # if lc > 10000:
    #     break

N = np.array(list(dic_word_context_count.values())).sum()

import pickle

print('pickling dic_word_context_count')
pickle.dump(dic_word_context_count, open('t_c_Dic.pkl', 'wb'))
print('pickling dic_word_count')
pickle.dump(dic_word_count, open('t_Dic.pkl', 'wb'))
print('pickling dic_context_count')
pickle.dump(dic_context_count, open('c_Dic.pkl', 'wb'))
print('pickling N')
pickle.dump(N, open('n.pkl', 'wb'))

print('done!')
