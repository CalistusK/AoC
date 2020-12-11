#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read()

#do stuff
pInput = pInput.split(', ')
coords = [(0,0)]
facing = 0

for i in range(0,len(pInput)):
    facing = ((facing - 1) % 4 if pInput[i][:1] == 'L' else (facing + 1) % 4)
    move = int(pInput[i][1:])
    if (facing == 0):
        coords.append( (coords[i][0], coords[i][1] + move) ) #north
    elif (facing == 1):
        coords.append( (coords[i][0] + move, coords[i][1]) ) #east
    elif (facing == 2):
        coords.append( (coords[i][0], coords[i][1] - move) ) #south
    else:
        coords.append( (coords[i][0] - move, coords[i][1]) ) #west

print(abs(coords[-1][0]) + abs(coords[-1][1]))
