//puzzle setup
const fs = require('fs');
inputs = fs.readFileSync('../day2in.txt','utf8');

//do stuff
arr = inputs.split(',').map(Number);
i = 0;
op = arr[0];

while (op != 99)
{
    op = arr[i];
    if (op == 1) arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]];
    if (op == 2) arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]];
    i += 4;
}
console.log(arr[0]);