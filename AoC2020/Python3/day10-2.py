#puzzle setup
with open('./day10in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]
pInput.append(0)
pInput.sort()
pInput.append(pInput[-1] + 3)
memoDict = {}
omittable = []

for i in range(2,len(pInput)):
  if pInput[i] - pInput[i-1] == 1 and pInput[i] - pInput[i-2] == 2:
    omittable.append(pInput[i-1])

memoDict[tuple(omittable)] = pInput.copy()

for x in omittable:
  pInput.remove(x)

memoDict[tuple([])] = pInput.copy()

print(len(memoDict))