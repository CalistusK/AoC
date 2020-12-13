#puzzle setup
import math
with open('./day12in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
xpos = 0
ypos = 0
xway = 10
yway = 1
facing = 1

for i in range(0,len(pInput)):
  arg = pInput[i][0]
  val = int(pInput[i][1:])
  tempx = xway
  tempy = yway

  if arg == 'N':
    yway += val
  if arg == 'S':
    yway -= val
  if arg == 'E':
    xway += val
  if arg == 'W':
    xway -= val
  if arg == 'R':
    val = math.radians(val)
    xway = round(tempx * math.cos(-val) - tempy * math.sin(-val))
    yway = round(tempx * math.sin(-val) + tempy * math.cos(-val))
  if arg == 'L':
    val = math.radians(val)
    xway = round(tempx * math.cos(val) - tempy * math.sin(val))
    yway = round(tempx * math.sin(val) + tempy * math.cos(val))
  if arg == 'F':
    xpos += val * xway
    ypos += val * yway

print(abs(xpos) + abs(ypos))