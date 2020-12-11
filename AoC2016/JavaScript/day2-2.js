//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('../day2in.txt','utf8');
input = input.split(/\r?\n/);

//do stuff
const pad = [
            [2,0,'1'],
            [1,1,'2'],[2,1,'3'],[3,1,'4'],
            [0,2,'5'],[1,2,'6'],[2,2,'7'],[3,2,'8'],[4,2,'9'],
            [1,3,'A'],[2,3,'B'],[3,3,'C'],
            [2,4,'D']
            ];
var ans = '';

for (i in input)
{
    var coords = [0,2];
    for (j in input[i])
    {
        let curr = input[i][j];
        let x = coords[0];
        let y = coords[1];
        let xl, xh, yl, yh;
        if (y === 0 || y == 4) xl = 2, xh = 2;
        if (y == 1 || y == 3) xl = 1, xh = 3;
        if (y == 2) xl = 0, xh = 4;
        if (x === 0 || x == 4) yl = 2, yh = 2;
        if (x == 1 || x == 3) yl = 1, yh = 3;
        if (x == 2) yl = 0, yh = 4;
        if ( (curr == 'L' && coords[0] > xl)
            || (curr == 'R' && coords[0] < xh) )
        {
            curr == 'L' ? coords[0]-- : coords[0]++;
        }
        if ( (curr == 'U' && coords[1] > yl)
            || (curr == 'D' && coords[1] < yh) )
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
