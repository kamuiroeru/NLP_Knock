# -*- coding: utf-8 -*-


def rem_waste(inlis: list) -> iter:
    return filter(lambda s: s != '', map(lambda t: t.strip('.,!?;:()[]"').strip("'"), inlis))


f = open('./enwiki-20150112-400-r10-105752.txt')

with open('out80.txt', 'w') as fo:
    for line in f:
        line = line.rstrip().split()
        fo.write(' '.join(rem_waste(line)) + '\n')
