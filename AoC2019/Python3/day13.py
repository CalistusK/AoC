import math

#puzzle setup
with open('./day13in.txt','r') as pInput:
    pInput = pInput.read().split(',')
pInput = [int(x) for x in pInput]

#do stuff
#todo: refactor all try/except blocks
gameData = []
loopCount = 0
iterator = 0
relative = 0
opIn = 0

def fixIdx(bigidx):
    while (len(pInput) < bigidx + 1):
        pInput.append(0)

def setParamModes(arr,idx,p):
    while (len(str(p)) < iterator - 1):
        p = '0' + str(p)
    for x in range(1,len(str(p))+1):
        if (str(p)[-x] == '0'):
            fixIdx(arr[idx+x])
            params.append(arr[arr[idx+x]])
        elif (str(p)[-x] == '1'):
            fixIdx(idx+x)
            params.append(arr[idx+x])
        elif (str(p)[-x] == '2'):
            fixIdx(arr[idx+x] + relative)
            if (opcode == 3 or x == 3): #slightly different write scenario
                params.append(arr[idx+x] + relative)
                continue
            params.append(arr[arr[idx+x] + relative])

while loopCount < len(pInput):
    if (iterator != 0):
        while (iterator < 0):
            iterator += 1
            loopCount -= 1
        while (iterator > 0):
            iterator -= 1
            loopCount += 1
        continue
    params = []
    opcode = pInput[loopCount] % 100
    pmodes = math.floor(pInput[loopCount] / 100)
    if (opcode == 99):
        print('Exit opcode 99 at ptr ' + str(loopCount) + ', position 0 output: ' + str(pInput[0]))
        loopCount = len(pInput)
    elif (opcode == 1):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        try:
            fixIdx(params[2])
        except:
            params.append(pInput[loopCount+3])
            fixIdx(params[2])
        pInput[params[2]] = params[0] + params[1]
    elif (opcode == 2):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        try:
            fixIdx(params[2])
        except:
            params.append(pInput[loopCount+3])
            fixIdx(params[2])
        pInput[params[2]] = params[0] * params[1]
    elif (opcode == 3):
        iterator = 1
        setParamModes(pInput,loopCount,pmodes)
        #
        pInput[params[0]] = opIn
    elif (opcode == 4):
        iterator = 1
        setParamModes(pInput,loopCount,pmodes)
        #
        opOut = params[0]
        gameData.append(opOut)
    elif (opcode == 5):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        iterator = (params[1] - loopCount - 1 if params[0] != 0 else 2)
    elif (opcode == 6):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        iterator = (params[1] - loopCount - 1 if params[0] == 0 else 2)
    elif (opcode == 7):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        try:
            fixIdx(params[2])
        except:
            params.append(pInput[loopCount+3])
            fixIdx(params[2])
        pInput[params[2]] = (1 if params[0] < params[1] else 0)
    elif (opcode == 8):
        iterator = 3
        setParamModes(pInput,loopCount,pmodes)
        #
        try:
            fixIdx(params[2])
        except:
            params.append(pInput[loopCount+3])
            fixIdx(params[2])
        pInput[params[2]] = (1 if params[0] == params[1] else 0)
    elif (opcode == 9):
        iterator = 1
        setParamModes(pInput,loopCount,pmodes)
        #
        relative += params[0]
    else:
        print('Error: unknown opcode ' + str(opcode) + ' at position ' + str(loopCount))
        quit()

    loopCount += 1

count = 0
for i in range(2,len(gameData),3):
    if (gameData[i] == 2):
        count += 1
print(count)
