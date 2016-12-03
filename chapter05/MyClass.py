class Morph:
    def __init__(self):
        self.surface = ''
        self.base = ''
        self.pos = ''
        self.pos1 = ''


class Chunk:
    def __init__(self):
        self.morphs = Morph()
        self.dst = 0
        self.srcs = 0
