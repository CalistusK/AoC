//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day3in.txt','utf8');
input = input.split(/\r?\n/);

//do stuff
for (i in input) input[i] = input[i].trim().replace(/[ \t]{2,}/g,' ').split(' ').map(Number);
ct = 0;
for (i in input)
{
    let a = input[i][0];
    let b = input[i][1];
    let c = input[i][2];
    if (a + b > c && a + c > b && b + c > a) ct++;
}
console.log(ct);