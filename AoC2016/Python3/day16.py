#puzzle setup
pInput = '01111010110010011'
disk = 272  #input is 35651584 for part 2

#do stuff
checksum = ''

def getChecksum(cs):
    temp = ''
    for i in range(0,len(cs),2):
        if cs[i] == cs[i+1]:
            temp += '1'
        else:
            temp += '0'
    return temp

while len(pInput) < disk:
    pInput = pInput + '0' + pInput[::-1].replace('0','a').replace('1','0').replace('a','1')

checksum = pInput[:disk]

while len(checksum) % 2 == 0:
    checksum = getChecksum(checksum)

print(checksum)