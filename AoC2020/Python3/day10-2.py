#puzzle setup
with open('./day10in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]
pInput.append(0)
pInput.sort()
pInput.append(pInput[-1] + 3)
memoDict = {}

for x in pInput:
  if x == 0:
    memoDict[x] = 1
    continue

  memoDict[x] = memoDict.get(x-3,0) + memoDict.get(x-2,0) + memoDict.get(x-1,0)

print(memoDict[pInput[-1]])