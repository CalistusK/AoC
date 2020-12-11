#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read()

#do stuff
pInput = pInput.split(', ')
coords = [(0,0)]
facing = 0

def stepCheck(coord):
    if (len(coords) - coords[::-1].index(coord) - 1 != coords.index(coord)):
        print(abs(coord[0]) + abs(coord[1]))
        quit()

for i in range(0,len(pInput)):
    facing = ((facing - 1) % 4 if pInput[i][:1] == 'L' else (facing + 1) % 4)
    move = int(pInput[i][1:])
    if (facing == 0):
        for j in range(0,move):
            coords.append( (coords[-1][0], coords[-1][1] + 1) ) #north
            stepCheck(coords[-1])
    elif (facing == 1):
        for j in range(0,move):
            coords.append( (coords[-1][0] + 1, coords[-1][1]) ) #east
            stepCheck(coords[-1])
    elif (facing == 2):
        for j in range(0,move):
            coords.append( (coords[-1][0], coords[-1][1] - 1) ) #south
            stepCheck(coords[-1])
    else:
        for j in range(0,move):
            coords.append( (coords[-1][0] - 1, coords[-1][1]) ) #west
            stepCheck(coords[-1])
