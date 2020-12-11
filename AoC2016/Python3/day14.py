import hashlib
import re

#puzzle setup
pInput = 'ihaygndm'

#do stuff
i = 0
count = 0
c = ''
rx3 = re.compile(r'(\w)\1\1')
rx5 = re.compile(r'(\w)\1\1\1\1')

def nextThousand(sameNum,counter):
    for j in range(1,1001):
        okhash = pInput + str(i + j)
        okhash = hashlib.md5(okhash.encode()).hexdigest()
        okhash = rx5.search(okhash)
        if okhash and okhash[0][0] == sameNum:
            return counter + 1
    return counter

while (count < 64):
    hashed = pInput + str(i)
    hashed = hashlib.md5(hashed.encode()).hexdigest()
    hashed = rx3.search(hashed)
    if hashed:
        c = hashed[0][0]
        count = nextThousand(c,count)
        c = ''
    i += 1

print(i-1)
