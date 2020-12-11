//puzzle setup
const fs = require('fs');
input = fs.readFileSync('../day1in.txt','utf8');
arr = input.split(/\r?\n/);

//do stuff
sum = 0;
for (i in arr)
{
    sum += Math.floor(arr[i]/3) - 2;
}
console.log(sum);