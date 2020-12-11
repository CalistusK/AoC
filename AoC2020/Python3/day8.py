#puzzle setup
with open('./day8in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
acc = 0
i = 0
visited = []

while i not in visited:
  arg = pInput[i][:3]
  visited.append(i)

  if arg == 'nop':
    i += 1
    continue

  if arg == 'acc':
    acc += int(pInput[i][4:])
    i += 1
    continue
  
  if arg == 'jmp':
    i += int(pInput[i][4:])
    continue

print(acc)