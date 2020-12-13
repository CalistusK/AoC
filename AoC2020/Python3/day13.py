#puzzle setup
import math
import sys
with open('./day13in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput[0] = int(pInput[0])
pInput[1] = pInput[1].split(',')
pInput[1] = [int(x) for x in pInput[1] if x != 'x']
nearest = sys.maxsize

for x in pInput[1]:
  this = math.ceil(pInput[0] / x)
  if this * x - pInput[0] < nearest:
    nearest = this * x - pInput[0]
    nearestID = x

print(nearest * nearestID)