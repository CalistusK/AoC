#puzzle setup
with open('./day12in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
xpos = 0
ypos = 0
facing = 1

for i in range(0,len(pInput)):
  arg = pInput[i][0]
  val = int(pInput[i][1:])

  if arg == 'N':
    ypos += val
  if arg == 'S':
    ypos -= val
  if arg == 'E':
    xpos += val
  if arg == 'W':
    xpos -= val
  if arg == 'L':
    facing = (facing - val / 90) % 4
  if arg == 'R':
    facing = (facing + val / 90) % 4
  if arg == 'F':
    if facing == 0:
      ypos += val
    if facing == 1:
      xpos += val
    if facing == 2:
      ypos -= val
    if facing == 3:
      xpos -= val

print(abs(xpos) + abs(ypos))