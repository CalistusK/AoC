#puzzle setup
with open('./day4in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
pInput = [x.replace('-',' ')[:-7] for x in pInput]
shiftarr = []

def rot(s,n):
    shifted = ''
    for i in range(len(s)):
        if s[i] == ' ':
            shifted += ' '
            continue
        shifted += chr((ord(s[i]) + n - 97) % 26 + 97)
    return shifted

for x in pInput:
    x = rot(x[:-4],int(x[-3:])) + ' ' + x[-3:]
    if 'north' in x:
        print(x)
