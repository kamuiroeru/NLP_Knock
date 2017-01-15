from pprint import pprint

from k54 import load_xml
import re

parse_strings = [sentences['parse'] for sentences in load_xml()['root']['document']['sentences']['sentence']]

# pprint(parse_strings)

for ps in parse_strings:
    start = 0
    while len(ps) > start:
        start += 1
        if ps[start:start+3] == '(NP':
            end, count = start, 1
            while count:
                end += 1
                if ps[end] == '(':
                    count += 1
                elif ps[end] == ')':
                    count -= 1

            out = []
            for word in ps[start:end+1].split(' '):
                if word and word[-1] == ')':
                    out.append(word.replace(')', ''))

            print(' '.join(out))
    # out = [word.replace(')', '') for word in words if word[-1] == ')']
    # print(' '.join(out))

        # count, npCount, npPos = 0, 0, []
        # strList = ['']
        # for s in ps.split(' '):
        #     if s[0] == '(':
        #         count += 1
        #         if s == '(NP':
        #             npCount += 1
        #             npPos.append((npCount, count))
        #             strList.append('')
        #     else:
        #         for hoge in range(s.count(')')):
        #             count -= 1
        #             if npPos:
        #                 if npPos[-1][1] <= count:
        #                     for np in npPos:
        #                         strList[np[0]] += s.replace(')', '') + ' '
        #                 if npPos[-1][1] > count:
        #                     npPos.pop()
        # print(strList)



        # ps = ps.replace(') (', '},{') \
        #     .replace(' ', ':') \
        #     .replace('(', '{') \
        #     .replace(')', '}')
        # psJson = re.sub(r'\w\W')
        # print(ps)

        # stackL, stackS, step = [[]] * 20, [[]] * 20, 0
        # temp = ''
        # print(ps)
        # n = 0
        # while n < len(ps):
        #     if ps[n] == '(':
        #         n += 1
        #         label = ''
        #         while ps[n] != ' ':
        #             label += ps[n]
        #             n += 1
        #         step += 1
        #         stackL[step].append(label)
        #     elif ps[n] == ')':
        #         s = ''
        #         while ps[n] != ')':
        #             s += ps[n]
        #             n += 1
        #         step -= 1
        #         stackS[step].append(s)
        #     n += 1
        # print(stackL)
        # print(stackS)
#
#         elif s[n] == ')':
#         step -= 1
#     elif s[n] == ' ':
#     stack[step] += ','
# else:
#     stack[step] += s
# for s in ps:
#     # print(s)
#     if s == '(':
#         step += 1
#     elif s == ')':
#         step -= 1
#     elif s == ' ':
#         stack[step] += ','
#     else:
#         stack[step] += s
# print(stack)
