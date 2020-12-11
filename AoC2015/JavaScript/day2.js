//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day2in.txt', 'utf8');
input = input.split(/\r?\n/);

//do stuff
var sum = 0;
for (i in input) input[i] = input[i].split('x').map(Number);

for (let i = 0; i < input.length; i++)
{
    let temp = [];
    temp.push(input[i][0] * input[i][1]); // l*w
    temp.push(input[i][1] * input[i][2]); // w*h
    temp.push(input[i][2] * input[i][0]); // h*l
    let small = Math.min(...temp);
    sum += small;
    sum += temp.reduce((a,b)=>a+b,0) * 2;
}
console.log(sum);