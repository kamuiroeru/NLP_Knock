import JsonAdapter


class Morph(JsonAdapter.JsonAdapter):
    def __init__(self):
        self.surface = ''
        self.base = ''
        self.pos = ''
        self.pos1 = ''