import math

#puzzle setup
pInput = open('../day5in.txt','r').read().split(',')
pInput = [int(x) for x in pInput]
#pInput = [1002,4,3,4,33]

#do stuff
iterator = 0
opIn = 5 #technically part of puzzle setup

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
    elif (opcode == 5):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        iterator = (params[1] - i - 1 if params[0] != 0 else 2)
    elif (opcode == 6):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        iterator = (params[1] - i - 1 if params[0] == 0 else 2)
    elif (opcode == 7):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        pInput[pInput[i+3]] = (1 if params[0] < params[1] else 0)
    elif (opcode == 8):
        iterator = 3
        setParamModes(pInput,i,pmodes)
        #
        pInput[pInput[i+3]] = (1 if params[0] == params[1] else 0)
    else:
        print('Error: unknown opcode ' + str(opcode) + ' at position ' + str(i))
        quit()