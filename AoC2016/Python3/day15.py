#puzzle setup
pInput = [7,13,3,5,17,19]
pPos = [0,0,2,2,0,7]

#do stuff
time = 0
goal = [6,11,0,1,12,13]

while pPos != goal:
    time += 1
    for i in range(0,len(pPos)):
        pPos[i] = (pPos[i] + 1) % pInput[i]

print(time)
