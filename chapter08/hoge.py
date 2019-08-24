# coding: utf-8
import numpy as np
np.inner([1,2,3],[4,5,6])
l = [1,2]
l[3]
dir(tuple())
dir(list())
dir(str())
[1,2] + [2,3]
from subprocess import getoutput
getoutput('ls)
getoutput('ls')
print(getoutput('ls'))
getoutput('head -n1 sentiment.txt')
getoutput('head -n1 sentiment.txt|tail -n1')
getoutput('head -n2 sentiment.txt|tail -n1')
getoutput('head -n3 sentiment.txt|tail -n1')
getoutput('head -n{} {}|tail -n1'.format(3, 'setntiment.txt'))
getoutput('head -n{} {}|tail -n1'.format(3, 'sentiment.txt'))
np.ndarray(10).reshape(2,5)
np.zeros(range(10)).reshape(2,5)
np.zeros(10).reshape(2,5)
a,b,c,d = [1,2,3,4]
a
b
c
d
from collections import Counter
from random import choices
from random import randint
randint(1,5)
randint(1,5,10)
cou = Counter([1,2,3,4,1,2,3,4,2,3,4,5,4,3,3])
list(map(lambda x: cou[x], [1,2,3])
)
cou
map(lambda x: cou[x], [1,2,3])
a,b,c = map(lambda x: cou[x], [1,2,3])
a
b
c
l = choice(['hoge', 'huga', 'pyo'])
from random import choice
choice(range(10), 10)
choice(range(10), 10, 100)
choice(range(10))
choice(range(10))
choice(range(10), k=10)
from random import randint
randint(0,10,10)
randint(0,100,10)
from numpy.random import randint
randint(0,10,100)
from collections import Counter
from random import randint
l = randint(0,5,10)
from collections import Counter
from numpy.random import randint
l = randint(0,5,10)
l
Counter(l)
list(range(0,10,3))
l = list(range(10))
l
[l[i:i + 3] for i in range(0,10,3)]
10 // 3
inputList = open('sentiment.txt')
inputList = [line.rstrip() for line in open('sentiment.txt')]
len(inputList)
len(inputList) // 5
s = len(inputList) // 5
L = [inputList[i:i+s] for i in range(0, len(inputList), s)]
L
len(L)
L[-1] = L[-2] + L[-1]
len(L)
L
L[-2] = L[-1]
L = L[:-1]
len(L)
[]*4
z,x,c,v = []
z,x,c,v = []*4
z,x,c,v = [[]]*4
z
[[]]*4
l
for i in range(10):
    print(l[:i] + l[i+1:])
    
for i in range(10):
    print(l[i], l[:i] + l[i+1:])
    
L
get_ipython().magic('time L')
get_ipython().magic('time [ x for l in L for x in l]')
def fl(lists:list, n=10):
    hoge = [x for l in lists for x in l]
    
get_ipython().magic('time fl(L)')
get_ipython().magic('time fl(L, 10000)')
get_ipython().magic('time fl(L, 100000000)')
get_ipython().magic('time fl(L, 100000000000)')
get_ipython().magic('time fl(L, 1000000)')
get_ipython().magic('time fl(L, 10)')
get_ipython().magic('time fl(L, 1)')
from itertools import flatten
from itertools import chain
def ch(lists:list, n=10):
    hoge = chain(lists)
    
get_ipython().magic('time ch(L)')
get_ipython().magic('time ch(L, 100000)')
get_ipython().magic('time ch(L, 1000000000)')
open('./sentiment.txt').readlines()
a,b,c = [1,2,3,4]
average([1,2,3,4])
a,b,c,d = np.zeros(5) * 4
a,b,c,d = np.zeros(5 * 4).reshape(4, 5)
a
np.average(a)
np.array(['hoge', 'huga', 'pyo'])
np.array(['hoge', 'huga', 'pyo'])
np.array(['hoge', 'huga', 'pyo'])[-1]
border = 1
list(range(0,1,0.1))
list(range(0,1.0,0.1))
np.arange(10)
np.arange(0,10)
np.arange(0,1,0.1)
np.arange(0,1,0.01)
np.arange(0,1,1/10)
np.arange(0,1,1/100)
import pandas as pd
lrand = np.random.randint(0,100,10)
lrand
sorted(lrand)
sorted(lrand, reverse=True)
pd.read_table('./k76output.txt')
df =pd.read_table('./k76output.txt')
df.columns['ans', 'prediction', 'odds']
df.columns = ['ans', 'prediction', 'odds']
df[['ans', 'odds']]
for a, o in df[['ans', 'odds']]:
    print(a,o)
    
for a, o in df[['ans', 'odds']].iterrows():
    print(a,o)
    
for a, o in df[['ans', 'odds']].iterrows():
    print(int(a),o)
    
for a, o in df[['ans', 'odds']].iterrows():
    print(type(a))
    
for a, o in df[['ans', 'odds']].iterrows():
    print(type(o))
    
for k, o in df[['ans', 'odds']].iterrows():
    print(o['ans'])
    
for k, o in df[['ans', 'odds']].iterrows():
    print(int(o['ans']))
    
for k, o in df[['ans', 'odds']].iterrows():
    print(int(o['ans']), float(o['odds']))
    
df.plot()
df.plot()
df.plot(y=['ans', 'odds'])
import matplotlib
import matplotlib.pyplot as plt
df.plot(y=['ans', 'odds'])
df.plot(y=['ans', 'odds'])plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
plt.style.use('ggplot') 
font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)
df.plot(y=['ans', 'odds'])plt.style.use('ggplot')
df.plot(y=['ans', 'odds'])
np.arange(10).length
np.arange(10).length()
len(np.arange(10))
l = [[1,2,3],[4,5,6]]
l
[1,2,3,4,5,6]
templist = l
[i for l in templist for i in l]
for l in templist:
    for i in l:
        print(i, end=' ')
        
C = 5
N = 100
fi = list(range(100))
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    
outList = []
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList
outList
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
C = 2
N = 10
fi = list(range(10))
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList = []
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList
C = 5
N = 10
fi = list(range(10))
outList = []
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList
C = 5
N = 13
outList = []
fi = list(range(13))
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList
C = 5
N = 10662
fi = list(range(10662))
outList = []
for i in range(C):
    splited_list = fi[i * round(N / C):(i + 1) * round(N / C)] if i < C - 1 else fi[i * round(N / C):N]
    outList.append(splited_list)
    
outList
outList[-1]
len(outList[-1])
len(outList[-2])
len(outList[-3])
len(outList[-4])
len(outList[-5])
len(outList[-6])
np.array([1,1.2,2,3.4])
np.array([1,1.2,2,3.4]).dtype
def retEnt(a,b,c,d)
from math import log2
def retEnt(inlis):
    return sum([i * log2(i) for i in inlis])
retEnt([1/2, 1/4, 1/8, 1/8])
retEnt([3/4, 1/8, 1/8])
log2(2)
log2(1/4)
def retEnt(inlis):
    return sum([-i * log2(i) for i in inlis])
retEnt([1/2, 1/4, 1/8, 1/8])
retEnt([3/4, 1/8, 1/8])
log2(1/3)
log2(1/3) * 3
retEnt([0.2,0.8])
retEnt([0.5,0.5])
5 * 0.72 + 8
11.6/13
get_ipython().magic('quickref')
get_ipython().magic('save chapter08andlog.py')
get_ipython().magic('hist')
get_ipython().magic('save hoge.py')
get_ipython().magic('save')
get_ipython().magic('save ?')
get_ipython().magic('pinfo save')
get_ipython().magic('save -f hoge.py')
get_ipython().magic('save -f hoge.py')
get_ipython().magic('save hoge.py')
get_ipython().magic('save hoge.py -')
get_ipython().magic('save hoge.py 1-100')
from os import ls
from os import listdir
listdir()
get_ipython().magic('save hoge.py 1-')
get_ipython().magic('save hoge.py 1-240')
