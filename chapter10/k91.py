# coding: utf-8

# import json
instr = open('./questions-words.txt').read()
instr
sections = [section.split('\n') for section in instr.split(':')]
sectionsDic = {l[0].strip(): l[1:] for l in sections}

open('out91.txt', 'w').write('\n'.join(sectionsDic['family']))
