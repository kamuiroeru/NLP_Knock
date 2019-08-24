from MyClass import Morph

j = {"test2": {"num": 200, "str": "def"}, "num": 100, "str": "abc"}

a = Morph()
print(a.__dict__)
a.base = 'hogehoge'
a.surface = 'fugafuga'

print(a.__dict__)
# a.serialize(j)
# print(a.to_json())

b = lambda: 1
b.a = 1
print(b.__dict__)
print(b())