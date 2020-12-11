#puzzle setup
import math
with open('./day5in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
high = 0

for i in range(0,len(pInput)):
  minrow = 0
  mincol = 0
  maxcol = 7
  maxrow = 127
  finalrow = 0
  finalcol = 0

  for j in range(0,7):
    if pInput[i][j] == 'F':
      maxrow -= math.ceil((maxrow-minrow)/2)
      if j == 6:
        finalrow = minrow
    if pInput[i][j] == 'B':
      minrow += math.ceil((maxrow-minrow)/2)
      if j == 6:
        finalrow = maxrow

  for j in range(7,10):
    if pInput[i][j] == 'L':
      maxcol -= math.ceil((maxcol-mincol)/2)
      if j == 9:
        finalcol = mincol
    if pInput[i][j] == 'R':
      mincol += math.ceil((maxcol-mincol)/2)
      if j == 9:
        finalcol = maxcol

  if (finalrow * 8) + finalcol > high:
    high = (finalrow * 8) + finalcol

print(high)