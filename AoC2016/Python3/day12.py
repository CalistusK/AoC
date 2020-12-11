#puzzle setup
pInput = open('AoC2016/day12in.txt','r').read().splitlines()

#do stuff
inst = 0
regs = [0,0,0,0] #a,b,c,d

def cpy(f,t): #copy from f, to t

def inc(n): #increase by n

def dec(n): #decrease by n

def jnz(x,n): #if x != 0, jump n from current

def parse(x): #return reg value or just int

while (inst < len(pInput)):
    curr = pInput[inst].split('')
    if curr[0] == 'cpy':
        copy(curr[1],curr[2])
    elif curr[0] == 'inc':
        inc(curr[1])
    elif curr[0] == 'dec':
        dec(curr[1])
    elif curr[0] == 'jnz':
        jnz(curr[1],curr[2])