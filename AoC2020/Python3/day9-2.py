#puzzle setup
with open('./day9in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]

for i in range(26,len(pInput)):
  found = False
  scopy = pInput[i-26:i].copy()
  scopy.sort()
  l = 0
  r = len(scopy) - 1

  for j in range(0,len(scopy)):
    if found == True:
      break

    while l < r:
      if scopy[l] + scopy[r] == pInput[i]:
        found = True
        break
      elif scopy[l] + scopy[r] < pInput[i]:
        l += 1
      else:
        r -= 1
    
    if found == False:
      partOne = pInput[i]

first = 0
for i in range(0,len(pInput)):
  if sum(pInput[first:i]) < partOne:
    continue
  
  while sum(pInput[first:i]) > partOne:
    first += 1
  
  if sum(pInput[first:i]) == partOne and len(pInput[first:i]) > 1:
    small = min(pInput[first:i])
    large = max(pInput[first:i])
    print(small + large)