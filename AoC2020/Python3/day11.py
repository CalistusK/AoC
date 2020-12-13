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
          if (ay != 0 or ax != 0) and ylen > y+ay >= 0 and xlen > x+ax >= 0 and inp[y+ay][x+ax] == '#':
            occ += 1

      if occ == 0 and inp[y][x] == 'L':
        pInput[y][x] = '#'
      if occ >= 4 and inp[y][x] == '#':
        pInput[y][x] = 'L'

  return inp == pInput

same = False

while not same:
  snapshot = copy.deepcopy(pInput)
  same = apply(snapshot)

pInput = ''.join([[''.join(x)][0] for x in pInput])
print(pInput.count('#'))