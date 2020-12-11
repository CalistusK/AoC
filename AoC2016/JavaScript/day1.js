//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day1in.txt','utf8');
input = input.split(', ');

//do stuff
var coords = [[0,0]];
var facing = 0; //0 = north, 1 = east, 2 = south, 3 = west
for (let i = 0; i < input.length; i++)
{
    newFacing(input[i]);
    let curr = [...coords[i]];
    let steps = Number(input[i].substring(1));
    switch(facing)
    {
        case 0:
            curr[1]+=steps;
            coords.push(curr);
            break;
        case 1:
            curr[0]+=steps;
            coords.push(curr);
            break;
        case 2:
            curr[1]-=steps;
            coords.push(curr);
            break;
        case 3:
            curr[0]-=steps;
            coords.push(curr);
            break;
    }
}
console.log(coords[coords.length-1].reduce((a,b)=>Math.abs(a)+Math.abs(b)));

function newFacing(n)
{
    let change = n.substring(0,1);
    if (change === 'R')
    {
        facing < 3 ? facing++ : facing = 0;
    } else {
        facing > 0 ? facing-- : facing = 3;
    }
}
