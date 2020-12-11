import re

#puzzle setup
with open('./day7in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
mysum = 0
abba = r'(?!(\w)\1\1\1)(\w)(\w)\3\2'

def checkBrackets(matches):
    for j in matches:
        if re.findall(abba,j):
            return True
    return False

for i in pInput:
    par = re.findall(r'\[(.*?)\]',i)
    if (checkBrackets(par)): #rule out cases based on brackets first
        continue

    m = re.findall(abba,i)
    if m:
        mysum += 1

print(mysum)
