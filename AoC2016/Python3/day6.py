import collections
#puzzle setup
with open('./day6in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
arr = ['','','','','','','','']
ans = ''

def getChars(idx):
    for x in pInput:
        arr[idx] += x[idx]

for i in range(0,len(pInput[0])):
    getChars(i)

for y in arr:
    ans += collections.Counter(y).most_common(1)[0][0]

print(ans)
