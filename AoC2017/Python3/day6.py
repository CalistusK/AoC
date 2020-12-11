#puzzle setup
with open('./day6in.txt','r') as pInput:
  pInput = pInput.read().split()

#do stuff
pInput = [int(x) for x in pInput]
states = []
acc = 0

while pInput not in states:
  findmax = pInput.copy()
  findmax.sort()
  high = findmax[-1]
  idx = pInput.index(high)
  print('break')