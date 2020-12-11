#puzzle setup
with open('./day6in.txt','r') as pInput:
  pInput = pInput.read().split('\n\n')

#do stuff
pInput = [x.replace('\n','') for x in pInput]
total = 0

for x in pInput:
  total += len(set(x))

print(total)