//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day2in.txt','utf8');
input = input.split(/\r?\n/);

//do stuff
const pad = [
            [0,0,'1'],[1,0,'2'],[2,0,'3'],
            [0,1,'4'],[1,1,'5'],[2,1,'6'],
            [0,2,'7'],[1,2,'8'],[2,2,'9']
            ];
var ans = '';

for (i in input)
{
    var coords = [1,1];
    for (j in input[i])
    {
        let curr = input[i][j];
        if ( (curr == 'L' && coords[0] > 0)
            || (curr == 'R' && coords[0] < 2) )
        {
            curr == 'L' ? coords[0]-- : coords[0]++;
        }
        if ( (curr == 'U' && coords[1] > 0)
            || (curr == 'D' && coords[1] < 2) )
        {
            curr == 'U' ? coords[1]-- : coords[1]++;
        }
    }
    for (i in pad)
    {
        if (pad[i][0] == coords[0] && pad[i][1] == coords[1]) ans+=pad[i][2];
    }
}
console.log(ans);