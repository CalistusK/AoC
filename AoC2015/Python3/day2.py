import numpy

#puzzle setup
with open('./day2in.txt','r') as pInput:
    pInput = pInput.read().splitlines(0)

#do stuff
mysum = 0
pInput = [i.split('x') for i in pInput]

for x in pInput:
    x = [int(i) for i in x]
    temp = []
    temp.append(x[0] * x[1])
    temp.append(x[0] * x[2])
    temp.append(x[1] * x[2])
    mysum += min(temp)
    mysum += numpy.sum(temp) * 2

print(mysum)
