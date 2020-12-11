import numpy

#puzzle setup
with open('./day2in.txt','r') as pInput:
    pInput = pInput.read().splitlines(0)

#do stuff
mysum = 0
pInput = [i.split('x') for i in pInput]

for x in pInput:
    x = [int(i) for i in x]
    mysum += numpy.prod(x)
    mysum += x.pop(x.index(min(x))) * 2
    mysum += min(x) * 2

print(mysum)
