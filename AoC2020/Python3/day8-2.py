#puzzle setup
with open('./day8in.txt','r') as pInput:
  pInput = pInput.read().splitlines()

#do stuff
acc = 0
i = 0
visited = []

def tryPatch(idx,targ,tacc):
  patchVisited = []
  patchInput = pInput.copy()
  patchAcc = tacc
  fix = 'nop' if targ == 'jmp' else 'jmp'

  patchInput[idx] = fix + patchInput[idx][3:]

  try:
    while idx not in patchVisited:
      targ = patchInput[idx][:3]
      patchVisited.append(idx)

      if targ == 'nop':
        idx += 1
        continue

      if targ == 'acc':
        tacc += int(patchInput[idx][4:])
        idx += 1
        continue
      
      if targ == 'jmp':
        idx += int(patchInput[idx][4:])
        continue
  except IndexError:
    print(tacc)

while i not in visited:
  arg = pInput[i][:3]
  visited.append(i)

  if arg == 'nop':
    tryPatch(i,arg,acc)
    i += 1
    continue

  if arg == 'acc':
    acc += int(pInput[i][4:])
    i += 1
    continue
  
  if arg == 'jmp':
    tryPatch(i,arg,acc)
    i += int(pInput[i][4:])
    continue