import hashlib

#puzzle setup
pInput = 'abbhdwsy'

#do stuff
ans = ''
count = 0

while (len(ans) < 8):
    hashed = pInput + str(count)
    hashed = hashlib.md5(hashed.encode()).hexdigest()
    if (hashed[:5] == '00000'):
        ans += hashed[5:6]
    count += 1

print(ans)