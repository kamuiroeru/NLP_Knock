import k88modNonzero
from sys import argv


spain = k88modNonzero.decompMat[k88modNonzero.label['Spain']]
madrid = k88modNonzero.decompMat[k88modNonzero.label['Madrid']]
athens = k88modNonzero.decompMat[k88modNonzero.label['Athens']]

if len(argv) == 4:
    spain = k88modNonzero.decompMat[k88modNonzero.label[argv[1]]]
    madrid = k88modNonzero.decompMat[k88modNonzero.label[argv[2]]]
    athens = k88modNonzero.decompMat[k88modNonzero.label[argv[3]]]

k88modNonzero.array = spain - madrid + athens

checkDic = k88modNonzero.procedure()

best10 = sorted(checkDic, key=lambda x: x[1], reverse=True)[1:11]

for word, cos in best10:
    print('{}\t\t{:0.2f}'.format(word, cos))
