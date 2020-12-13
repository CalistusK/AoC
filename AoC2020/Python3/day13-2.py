#puzzle setup
import math
with open('./day13in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
del pInput[0]
pInput = pInput[0].split(',')
timeDict = {}
base = int(pInput[0])
inc = base
acc = 1

for x in pInput:
  if x != 'x':
    timeDict[int(x)] = pInput.index(x)

pair = []
while len(pair) < 2:
  while (base * acc + list(timeDict.values())[1]) % list(timeDict)[1] != 0:
    acc += 1
  pair.append(base * acc)
  acc += 1

inc = pair[1] - pair[0]
base = pair[1]

for i in range(2,len(timeDict)):
  pair = []
  acc = 1
  while len(pair) < 2:
    if i == len(timeDict) - 1 and len(pair) == 1:
      print(pair[0])
      exit()
    thisVal = list(timeDict.values())[i]
    thisKey = list(timeDict)[i]
    while (base + (inc * acc) + thisVal) % thisKey != 0:
      acc += 1
    pair.append(base + (inc * acc))
    acc += 1
  base = pair[1]
  inc = pair[1] - pair[0]