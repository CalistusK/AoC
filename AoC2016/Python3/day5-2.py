import hashlib

#puzzle setup
pInput = 'abbhdwsy'

#do stuff
ans = ['','','','','','','','']
result = ''
count = 0

#takes a bit, but it gets there!
while (len(result.join(ans)) < 8):
    hashed = pInput + str(count)
    hashed = hashlib.md5(hashed.encode()).hexdigest()
    try:
        pos = int(hashed[5:6])
    except:
        count += 1
        continue
    if ((hashed[:5] == '00000') and (pos < len(ans))):
        if (ans[pos] == ''):
            ans[pos] += hashed[6:7]
    count += 1

print(result.join(ans))