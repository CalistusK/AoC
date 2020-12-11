#puzzle setup
with open('./day10in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]
pInput.append(0)
pInput.sort()
pInput.append(pInput[-1] + 3)
diffs = {1:0,2:0,3:0}

for i in range(1,len(pInput)):
  diff = pInput[i] - pInput[i-1]
  if diff == 1:
    diffs[1] += 1
  if diff == 2:
    diffs[2] += 1
  if diff == 3:
    diffs[3] += 1

print(diffs[1] * diffs[3])