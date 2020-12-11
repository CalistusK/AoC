#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
n = 0
y = []

while True:
    for i in range(0,len(pInput)):
        x = pInput[i]
        if x[0] == '+':
            n += int(x[1:])
            y.append(n)
        else:
            n -= int(x[1:])
            y.append(n)
