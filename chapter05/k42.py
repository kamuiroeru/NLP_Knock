from pprint import pprint

from makePickle import pickleLoad

input_sentence = pickleLoad('outchunk.pickle')

output_sentence = []
for bun in input_sentence:
    string = ''
    for chunks in bun:
        if chunks.dst != -1:
            origin = ''.join([morph.surface for morph in chunks.morphs])
            origin += ''.join([morph.surface for morph in bun[chunks.dst].morphs])
            string += origin + '\t'
    output_sentence.append(string)

pprint(output_sentence)
