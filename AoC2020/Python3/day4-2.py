#puzzle setup
with open('./day4in.txt','r') as pInput:
  pInput = pInput.read().split('\n\n')

#do stuff
pInput = [' '.join(x.split('\n')) for x in pInput]

valid = 0

for i in range(0,len(pInput)):
  fields = len(pInput[i].split(' '))

  if not (fields == 8 or (fields == 7 and pInput[i].count('cid:') == 0)):
    continue
  
  this = pInput[i].split(' ')
  this = [x.split(':') for x in this]
  this = dict(this)

  if int(this.get('byr')) < 1920 or int(this.get('byr')) > 2002:
    continue

  if int(this.get('iyr')) < 2010 or int(this.get('iyr')) > 2020:
    continue

  if int(this.get('eyr')) < 2020 or int(this.get('eyr')) > 2030:
    continue

  if not this.get('hgt')[-2:] == 'cm' and not this.get('hgt')[-2:] == 'in':
    continue
  if this.get('hgt')[-2:] == 'cm':
    if int(this.get('hgt')[:-2]) < 150 or int(this.get('hgt')[:-2]) > 193:
      continue
  if this.get('hgt')[-2:] == 'in':
    if int(this.get('hgt')[:-2]) < 59 or int(this.get('hgt')[:-2]) > 76:
      continue

  if not len(this.get('hcl')) == 7 and not this.get('hcl')[0] == '#':
    continue
  try:
    int(this.get('hcl')[1:],16)
  except ValueError:
    continue

  if this.get('ecl') not in ['amb','blu','brn','gry','grn','hzl','oth']:
    continue

  if not len(this.get('pid')) == 9:
    continue
  try:
    int(this.get('pid'))
  except ValueError:
    continue

  valid += 1
  

print(valid)