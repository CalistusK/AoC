#puzzle setup
with open('./day7in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
pInput = [x.replace(' bag,',',').replace(' bags,',',').replace(' bags.','').replace(' bag.','').replace(' bags','') for x in pInput]
pInput = [x.split(' contain ') for x in pInput]
bagDict = {}
seeking = {'shiny gold'}
prevlen = 0

for i in range(0,len(pInput)):
  bagDict[pInput[i][0]] = pInput[i][1]

while prevlen < len(seeking):
  prevlen = len(seeking)
  for key in bagDict:
    for x in seeking.copy():
      if x in bagDict.get(key):
        seeking.add(key)

print(len(seeking) - 1)