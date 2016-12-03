from makePickle import pickleDump
from k40 import create_morph

pickleDump(create_morph(), 'out.pickle')
