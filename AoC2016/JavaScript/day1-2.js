//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day1in.txt','utf8');
input = input.split(', ');

//do stuff
var coords = [[0,0]];
var curr = [...coords[0]];
var facing = 0; //0 = north, 1 = east, 2 = south, 3 = west
for (i in 8) {console.log(i)}
for (let i = 0; i < input.length; i++)
{
    newFacing(input[i]);
    let steps = Number(input[i].substring(1));
    let j = 0;
    switch(facing)
    {
        case 0:
            for (; j < steps; j++)
            {
                curr[1]++;
                beenThere(curr);
                coords.push([...curr]);
            }
            break;
        case 1:
            for (; j < steps; j++)
            {
                curr[0]++;
                beenThere(curr);
                coords.push([...curr]);
            }
            break;
        case 2:
            for (; j < steps; j++)
            {
                curr[1]--;
                beenThere(curr);
                coords.push([...curr]);
            }
            break;
        case 3:
            for (; j < steps; j++)
            {
                curr[0]--;
                beenThere(curr);
                coords.push([...curr]);
            }
            break;
    }
}

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

function beenThere(loc)
{
    let check = -1;
    for (i in coords)
    {
        if (coords[i][0] == loc[0] && coords[i][1] == loc[1]) check = i;
    }
    if (check > -1)
    {
        console.log(coords[check].reduce((a,b)=>Math.abs(a)+Math.abs(b)));
        process.exit(1);
    }
}
