#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read()

#do stuff
mysum = 0
for i, c in enumerate(pInput, 1):
    mysum = (mysum + 1 if c == '(' else mysum - 1)
    if (mysum == -1):
        print(i)
        quit()
