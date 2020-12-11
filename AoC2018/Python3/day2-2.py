from difflib import ndiff
#puzzle setup
with open('./day2in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
for i in range(0,len(pInput)):
    this = pInput[i]
    for j in range(i+1,len(pInput)):
        diff = ''.join(ndiff(this,pInput[j])).replace(' ','')
        if len(diff) == len(this) + 3:
            startdiff = diff.index('-')
            commons = diff[0:startdiff] + diff[startdiff+4:]
            print(commons)
            quit()
