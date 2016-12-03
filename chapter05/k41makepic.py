from k41 import create_chunk
from makePickle import pickleDump

pickleDump(create_chunk(), 'outchunk')
