//puzzle setup
const fs = require('fs');
input = fs.readFileSync('../day1in.txt','utf8');
arr = input.split(/\r?\n/);

//do stuff
ans = 0;
sum = 0;

for (let i = 0; i < arr.length; i++)
{
    ans += fuel(arr[i]);
}

function fuel(n) {
    nf = Math.floor(n/3) - 2;
    sum += nf;
    if (nf > 8) fuel(nf);
    return sum;
}

console.log(sum);