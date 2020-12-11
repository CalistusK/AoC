from collections import Counter
#puzzle setup
with open('./day2in.txt','r') as pInput:
    pInput = pInput.read().splitlines()

#do stuff
cTwo = 0
cThree = 0
nc2 = True
nc3 = True
for x in pInput:
    y = Counter(x).most_common()
    for v in y:
        if v[1] == 2 and nc2:
            cTwo += 1
            nc2 = False
        if v[1] == 3 and nc3:
            cThree += 1
            nc3 = False
    nc2 = True
    nc3 = True
print(cTwo * cThree)
