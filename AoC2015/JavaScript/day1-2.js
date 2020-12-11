//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day1in.txt','utf8');
input = input.split('');

//do stuff
sum = 0;

for (i in input)
{
    input[i] == '(' ? sum++ : sum--;
    if (sum === -1)
    {
        console.log(Number(i)+1);
        break;
    }
}
