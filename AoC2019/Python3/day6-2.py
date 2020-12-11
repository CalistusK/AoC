#setup
with open('./day6in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
oDict = {}
ct = 0
sYou = 'YOU'
pYou = []
sSan = 'SAN'
pSan = []
for x in pInput:
    oSplit = x.split(')')
    oDict[oSplit[1]] = oSplit[0]
while sSan != 'COM':
    pSan.append(oDict[sSan])
    sSan = oDict[sSan]
while sYou != 'COM':
    pYou.append(oDict[sYou])
    sYou = oDict[sYou]
print(len([x for x in pSan if x not in set(pYou)]) + len([x for x in pYou if x not in set(pSan)]))
