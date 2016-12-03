import re

from MyClass import Morph


def create_morph(cabocha_text_lattice='neko.txt.cabocha'):
    outer_list = []
    inner_list = []
    with open(cabocha_text_lattice) as f:
        for line in filter(lambda x: x[0] is not '*', f):
            elements = re.split('[,\t]', line.rstrip())
            if len(elements) == 1:
                outer_list.append(inner_list)
                inner_list = []
            else:
                morph = Morph()
                morph.surface = elements[0]
                morph.base = elements[7]
                morph.pos = elements[1]
                morph.pos1 = elements[2]
                inner_list.append(morph)
    return outer_list


if __name__ == '__main__':
    print(list(map(lambda x: x.surface, create_morph()[2])))
