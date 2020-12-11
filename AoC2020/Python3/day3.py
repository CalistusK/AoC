#puzzle setup
with open('./day3in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
trees = x = y = 0
size = len(pInput[0])

while y < len(pInput):
  if pInput[y][x % size] == '#':
    trees += 1
  x += 3
  y += 1

print(trees)