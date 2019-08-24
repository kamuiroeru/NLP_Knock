import k88mod
from sys import argv


spain = k88mod.decompMat[k88mod.label['Spain']]
madrid = k88mod.decompMat[k88mod.label['Madrid']]
athens = k88mod.decompMat[k88mod.label['Athens']]

if len(argv) == 4:
    spain = k88mod.decompMat[k88mod.label[argv[1]]]
    madrid = k88mod.decompMat[k88mod.label[argv[2]]]
    athens = k88mod.decompMat[k88mod.label[argv[3]]]

k88mod.array = spain - madrid + athens

checkDic = k88mod.procedure()

best10 = sorted(checkDic, key=lambda x: x[1], reverse=True)[1:11]

for word, cos in best10:
    print('{}\t\t{:0.2f}'.format(word, cos))
