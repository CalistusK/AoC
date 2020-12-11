import math

#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
mysum = 0

for x in pInput:
    mysum += math.floor(int(x) / 3) - 2

print(mysum)
