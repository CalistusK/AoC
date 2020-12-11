//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day3in.txt','utf8');
input = input.split(/\r?\n/);

//do stuff
for (i in input) input[i] = input[i].trim().replace(/[ \t]{2,}/g,' ').split(' ').map(Number);
var redo = [];
for (let i = 0; i < input.length; i+=3)
{
    let x = [];
    let y = [];
    let z = [];
    for (let j = 0; j < 3; j++)
    {
        x.push(input[i+j][0]);
        y.push(input[i+j][1]);
        z.push(input[i+j][2]);
    }
    redo.push(x);
    redo.push(y);
    redo.push(z);
}
ct = 0;
input = redo;
for (i in input)
{
    let a = input[i][0];
    let b = input[i][1];
    let c = input[i][2];
    if (a + b > c && a + c > b && b + c > a) ct++;
}
console.log(ct);