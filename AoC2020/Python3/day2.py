#puzzle setup
with open('./day2in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
ans = 0

for i in range(0,len(pInput)):
  parts = pInput[i].split(' ')
  counts = parts[0].split('-')
  low = int(counts[0])
  high = int(counts[1])
  tar = parts[1][0]
  pw = parts[2]
  ct = pw.count(tar)
  
  if ct >= low and ct <= high:
    ans += 1

print(ans)