import math

#puzzle setup
with open('./day10in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
asteroids = []
maxRads = 0

for i in range(0,len(pInput)):
    for j in range(0,len(pInput[i])):
        if pInput[i][j] == "#":
            asteroids.append((j,i))

for roid in asteroids:
    rads = []
    for k in range(0,len(asteroids)):
        if roid != asteroids[k]:
            currRad = math.atan2(roid[1] - asteroids[k][1], roid[0] - asteroids[k][0])
            if currRad not in rads:
                rads.append(currRad)
    if len(rads) > maxRads:
        maxRads = len(rads)

print(maxRads)