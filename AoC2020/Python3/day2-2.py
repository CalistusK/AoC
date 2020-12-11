#puzzle setup
with open('./day2in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
ans = 0

for i in range(0,len(pInput)):
  parts = pInput[i].split(' ')
  pos = parts[0].split('-')
  posOne = int(pos[0]) - 1
  posTwo = int(pos[1]) - 1
  tar = parts[1][0]
  pw = parts[2]
  
  if (pw[posOne] == tar) ^ (pw[posTwo] == tar):
    ans += 1

print(ans)