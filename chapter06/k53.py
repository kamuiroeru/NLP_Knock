import re
from sys import argv
from parse import parse

try:
    raw_text_directory = argv[1]
except IndexError:
    raw_text_directory = 'nlp.txt.xml'

for line in open(raw_text_directory):
    line = line.strip()
    word = parse('<word>{}</word>', line)
    if word:
        print(word[0])
