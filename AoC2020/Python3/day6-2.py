#puzzle setup
with open('./day6in.txt','r') as pInput:
  pInput = pInput.read().split('\n\n')

#do stuff
pInput = [x.replace('\n',' ') for x in pInput]
total = 0

for x in pInput:
  this = x.split()
  this = [set(y) for y in this]
  total += len(set.intersection(*this))

print(total)