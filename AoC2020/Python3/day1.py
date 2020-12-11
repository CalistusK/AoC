#puzzle setup
with open('./day1in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [int(x) for x in pInput]
pInput.sort()

l = 0
r = len(pInput) - 1

while l < r:
    if pInput[l] + pInput[r] == 2020:
        print(pInput[l] * pInput[r])
        break
    elif pInput[l] + pInput[r] < 2020:
        l += 1
    else:
        r -= 1