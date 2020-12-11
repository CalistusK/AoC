#puzzle setup
with open('./day3in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
wireA = pInput[0].split(',')
wireB = pInput[1].split(',')
wacoords = [(0,0)]
wbcoords = [(0,0)]
dirs = 'UDLR'
dircoords = [(0,1),(0,-1),(-1,0),(1,0)]

def wireStep(go,wire):
    for y in range(0,go):
        zips = zip(wire[-1],dircoords[dirs.index(x[:1])])
        wire.append(tuple([sum(zipped) for zipped in zips]))

for x in wireA:
    wireStep(int(x[1:]),wacoords)

for x in wireB:
    wireStep(int(x[1:]),wbcoords)

intersect = list(set(wacoords).intersection(set(wbcoords)))
intersect.remove((0,0))

iSteps = []
for x in intersect:
    stepA = wacoords.index(x)
    stepB = wbcoords.index(x)
    iSteps.append(stepA+stepB)

print(min(iSteps))
