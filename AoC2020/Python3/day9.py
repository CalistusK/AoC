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
      print(pInput[i])
      exit()