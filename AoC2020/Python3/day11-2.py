#puzzle setup
import copy
with open('./day11in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [[char for char in x] for x in pInput]

def apply(inp):
  ylen = len(inp)
  for y in range(0,ylen):
    xlen = len(inp[y])
    for x in range(0,xlen):
      occ = 0

      for ay in range(-1,2):
        for ax in range(-1,2):
          step = 1
          aymult = ay*step
          axmult = ax*step
          valid = (ay != 0 or ax != 0) and ylen > y+aymult >= 0 and xlen > x+axmult >= 0
          while valid and inp[y+aymult][x+axmult] == '.':
            step += 1
            aymult = ay*step
            axmult = ax*step
            valid = (ay != 0 or ax != 0) and ylen > y+aymult >= 0 and xlen > x+axmult >= 0
          if valid and inp[y+aymult][x+axmult] == '#':
            occ += 1
          else:
            continue

      if occ == 0 and inp[y][x] == 'L':
        pInput[y][x] = '#'
      if occ >= 5 and inp[y][x] == '#':
        pInput[y][x] = 'L'

  return inp == pInput

same = False

while not same:
  snapshot = copy.deepcopy(pInput)
  same = apply(snapshot)

pInput = ''.join([[''.join(x)][0] for x in pInput])
print(pInput.count('#'))