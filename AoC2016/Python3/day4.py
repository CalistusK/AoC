import collections
#puzzle setup
with open('./day4in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
pInput = [x.replace('-','').replace('[','').replace(']','') for x in pInput]
mysum = 0

for x in pInput:
    mc = ''
    y = collections.Counter(x[:-8]).most_common()
    y = sorted(y,key=lambda z: (-z[1],z[0]))
    for i in range(0,5):
        mc += y[i][0]
    if (mc == x[-5:]):
        mysum += int(x[-8:-5])

print(mysum)
