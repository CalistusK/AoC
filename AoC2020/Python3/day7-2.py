#puzzle setup
with open('./day7in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [x.replace(' bag,',',').replace(' bags,',',').replace(' bags.','').replace(' bag.','').replace(' bags','') for x in pInput]
pInput = [x.split(' contain ') for x in pInput]
pInput = [[x[0],x[1].split(', ')] for x in pInput]
bagDict = {}
total = 0

def recursiveBag(thisBag,ct):
  global total
  for nextbag in bagDict.get(thisBag):
    if nextbag == 'no other':
      return
    n = int(nextbag.split()[0])
    y = n * ct
    total += y
    recursiveBag(nextbag[2:],y)

for i in range(0,len(pInput)):
  bagDict[pInput[i][0]] = pInput[i][1]

for bag in bagDict.get('shiny gold'):
  x = int(bag.split()[0])
  total += x
  recursiveBag(bag[2:],x)

print(total)