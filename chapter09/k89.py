import k88mod

spain = k88mod.decompMat[k88mod.label['Spain']]
madrid = k88mod.decompMat[k88mod.label['Madrid']]
athens = k88mod.decompMat[k88mod.label['Athens']]

k88mod.array = spain - madrid + athens

checkDic = k88mod.procedure()

best10 = sorted(checkDic, key=lambda x: x[1], reverse=True)[1:11]

for word, cos in best10:
    print('{}\t\t{:0.2f}'.format(word, cos))
