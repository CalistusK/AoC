//puzzle setup
const fs = require('fs');
var input = fs.readFileSync('./day1in.txt', 'utf8');
var arr = input.split(',');

var sum = 0;
var nums = [0];
//part 2?
//var ans = null;

for (i in arr)
{
    switch (arr[i].charAt(0))
    {
        case "+":
            sum += Number(arr[i].substr(1));
            pushCheck(sum);
            break;
        case "-":
            sum -= Number(arr[i].substr(1));
            pushCheck(sum);
            break;
    }
    //part 2?
    //if (ans) break;
}
console.log(nums[nums.length-1]);

function pushCheck(n)
{
    nums.push(n);
    //part 2?
    //if (nums.indexOf(n) != Number(i)+1) ans = n;
}