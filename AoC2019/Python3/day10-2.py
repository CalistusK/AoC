import math
import numpy as np

#puzzle setup
with open('./day10in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
asteroids = []
degreeDists = {}
station = (11,11)

for i in range(0,len(pInput)):
    for j in range(0,len(pInput[i])):
        if pInput[i][j] == "#":
            asteroids.append((j,i))

for k in range(0,len(asteroids)):
    if station != asteroids[k]:
        currRad = math.atan2(station[1] - asteroids[k][1], station[0] - asteroids[k][0])
        currDeg = np.rad2deg(currRad)
        currDeg = ((currDeg + 270) % 360)
        currDist = np.sum(abs(np.subtract(station,asteroids[k])))
        if (currDeg not in degreeDists) or (degreeDists.get(currDeg)[0] > currDist):
            degreeDists[currDeg] = [currDist,asteroids[k]]

i = 1
for key in sorted(degreeDists.keys()):
    if i == 200:
        print("Asteroid #" + str(i))
        print(key)
        print(degreeDists[key])
    i += 1
