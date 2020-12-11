#puzzle setup
with open('./day1in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]
pInput.sort()

for i in range(0,len(pInput)):
  l = i + 1
  r = len(pInput) - 1
  while l < r:
      if pInput[l] + pInput[r] + pInput[i] == 2020:
          print(pInput[l] * pInput[r] * pInput[i])
          break
      elif pInput[l] + pInput[r] + pInput[i] < 2020:
          l += 1
      else:
          r -= 1
  i += 1