#puzzle setup
with open('./day1in.txt','r') as pInput:
    pInput = pInput.read()

#do stuff
mysum = 0
for c in pInput:
    mysum = (mysum + 1 if c == '(' else mysum - 1)
print(mysum)
