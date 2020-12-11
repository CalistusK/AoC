#puzzle setup
with open('./day4in.txt','r') as pInput:
  pInput = pInput.read().split('\n\n')

#do stuff
pInput = [' '.join(x.split('\n')) for x in pInput]

valid = 0

for i in range(0,len(pInput)):
  fields = len(pInput[i].split(' '))
  if fields == 8 or (fields == 7 and pInput[i].count('cid:') == 0):
    valid += 1

print(valid)