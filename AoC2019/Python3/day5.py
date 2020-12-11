import math

#puzzle setup
with open('./day5in.txt','r') as pInput:
    pInput = pInput.read().split(',')
pInput = [int(x) for x in pInput]
#pInput = [1002,4,3,4,33]

#do stuff
iterator = 0
opIn = 1 #technically part of puzzle setup

def setParamModes(arr,idx,p):
    while (len(str(p)) < iterator - 1):
        p = '0' + str(p)
    for x in range(1,len(str(p))+1):
        if (str(p)[-x] == '0'):
            params.append(arr[arr[idx+x]])
        elif (str(p)[-x] == '1'):
            params.append(arr[idx+x])

for i in range(0,len(pInput)):
    if (iterator > 0):
        iterator -= 1
        continue
    params = []
    opcode = pInput[i] % 100
    pmodes = math.floor(pInput[i] / 100)
    if (opcode == 99):
        print('Exit opcode 99 at ptr ' + str(i) + ', position 0 output: ' + str(pInput[0]))
        quit()
    elif (opcode == 1):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        pInput[pInput[i+3]] = params[0] + params[1]
    elif (opcode == 2):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        pInput[pInput[i+3]] = params[0] * params[1]
    elif (opcode == 3):
        iterator = 1
        setParamModes(pInput,i,pmodes)
        #
        pInput[pInput[i+1]] = opIn
    elif (opcode == 4):
        iterator = 1
        setParamModes(pInput,i,pmodes)
        #
        opOut = params[0]
        print('Opcode 4 output at i = ' + str(i) + ': ' + str(opOut))
    else:
        print('Error: unknown opcode ' + str(opcode) + ' at position ' + str(i))
        quit()
