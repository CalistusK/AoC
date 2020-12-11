//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day5in.txt','utf8');
input = input.split(/\r?\n/);

//do stuff
sum = 0;

for (i in input)
{
    if (!input[i].match(/(.)\1/g)) continue; //double letter
    if (!input[i].match(/[aeiou]/g) || (input[i].match(/[aeiou]/g)).length < 3) continue; //3 vowels
    if (input[i].match(/ab|cd|pq|xy/)) continue; //ab, cd, pq, xy
    sum++;
}
console.log(sum);