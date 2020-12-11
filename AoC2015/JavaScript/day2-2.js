//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day2in.txt', 'utf8');
input = input.split(/\r?\n/);

//do stuff
var sum = 0;
for (i in input) input[i] = input[i].split('x').map(Number);

for (let i = 0; i < input.length; i++)
{
    let small = Math.min(...input[i]);
    sum += small * 2; //smallest
    sum += Math.min(...delSmall(input[i])) * 2; //second smallest
    sum += input[i].reduce((a,b)=>a*b); //multiply all
}
console.log(sum);

function delSmall(arr)
{
    arr = [...arr];
    arr.splice(arr.indexOf(Math.min(...arr)),1)
    return arr;
}