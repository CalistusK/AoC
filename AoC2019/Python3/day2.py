#puzzle setup
with open('./day2in.txt','r') as pInput:
    pInput = pInput.read().split(',')
pInput = [int(x) for x in pInput]

#per puzzle instructions..
pInput[1] = 12
pInput[2] = 2

#do stuff
for i in range(0,len(pInput),4):
    opcode = pInput[i]
    valA = pInput[i+1]
    valB = pInput[i+2]
    resultPos = pInput[i+3]

    if (opcode == 99):
        print('Exit opcode 99, position 0 output: ' + str(pInput[0]))
        quit()
    elif (opcode == 1):
        pInput[resultPos] = pInput[valA] + pInput[valB]
    elif (opcode == 2):
        pInput[resultPos] = pInput[valA] * pInput[valB]
    else:
        print('Error: unknown opcode ' + str(opcode) + ' at position ' + str(i))
        quit()
