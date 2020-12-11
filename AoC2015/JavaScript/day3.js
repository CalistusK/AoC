//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day3in.txt', 'utf8');
input = input.split('');

//do stuff
ans = [[0,0,1]];
pos = 0;

for (let i = 0; i < input.length; i++)
{
    let temp = [0];
    temp.unshift(ans[pos][0],ans[pos][1]);
    switch(input[i])
    {
        case "^":
            temp[1]++;
            break;
        case "v":
            temp[1]--;
            break;
        case "<":
            temp[0]--;
            break;
        case ">":
            temp[0]++;
            break;
    }
    beenThere(temp);
}
console.log(ans.length)

function beenThere(arr)
{
    for (i in ans)
    {
        if (ans[i][0]==arr[0]&&ans[i][1]==arr[1])
        {
            ans[i][2]++;
            pos = i;
            return;
        }
    }
    arr[2] = 1;
    ans.push(arr);
    pos = ans.length - 1;
    return;
}