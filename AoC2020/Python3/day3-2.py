#puzzle setup
import math
with open('./day3in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
size = len(pInput[0])
results = []

def getTrees(xvel,yvel):
  trees = x = y = 0

  while y < len(pInput):
    if pInput[y][x % size] == '#':
      trees += 1
    x += xvel
    y += yvel
  
  results.append(trees)

getTrees(1,1)
getTrees(3,1)
getTrees(5,1)
getTrees(7,1)
getTrees(1,2)

print(math.prod(results))