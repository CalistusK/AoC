import math

#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
mysum = 0

for x in pInput:
    while int(x) > 5:
        x = math.floor(int(x) / 3) - 2
        mysum += x

print(mysum)
