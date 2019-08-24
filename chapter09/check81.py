# coding: utf-8
templist = []
for line in open('./useList.txt'):
    line = line.rstrip().split(' ')
    if len(line) > 1:
        templist.append(' '.join(line))

searchStr = '|'.join(templist)
searchStr
import re
re.match('Isle of Man is beautiful site', searchStr)
searchStr = "[" + searchStr + ']'
re.match('Isle of Man is beautiful site', searchStr)
searchStr
searchStr = searchStr[1:]
searchStr = searchStr[:-1]
searchStr
re.match(searchStr, 'Isle of Man is beautiful site')
re.match(searchStr, 'Isle of Man is beautiful site').group()
re.match(searchStr, 'Isle of Man is beautiful site and United States is country').group()
re.match(searchStr, 'Isle of Man is beautiful site and United States is country')
re.finditer(searchStr, 'Isle of Man is beautiful site and United States is country')
for v in re.finditer(searchStr, 'Isle of Man is beautiful site and United States is country')
for v in re.finditer(searchStr, 'Isle of Man is beautiful site and United States is country'):
    print(v.group())
    
for v in re.findall(searchStr, 'Isle of Man is beautiful site and United States is country'):
    print(v.group())
    
for v in re.findall(searchStr, 'Isle of Man is beautiful site and United States is country'):
    print(v)
    
for matchStr in re.findall(searchStr, line.rstrip()):
    line = line.replace(matchStr, '_'.join(matchStr.split()))
    
line = 'Isle of Man is beautiful site and United States is country'
for matchStr in re.findall(searchStr, line.rstrip()):
    line = line.replace(matchStr, '_'.join(matchStr.split()))
    
line
line = 'Isle of Man is beautiful site and United States is country\n'
line
print(line)
for matchStr in re.findall(searchStr, line.rstrip()):
    line = line.replace(matchStr, '_'.join(matchStr.split()))
    
print(line)
get_ipython().magic('save check81.py 1-29')
