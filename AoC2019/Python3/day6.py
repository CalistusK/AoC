#setup
with open('./day6in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
oDict = {}
ct = 0
for x in pInput:
    oSplit = x.split(')')
    oDict[oSplit[1]] = oSplit[0]
for x in pInput:
    y = x.split(')')[1]
    while y != 'COM':
        y = oDict[y]
        ct += 1
print(ct)
