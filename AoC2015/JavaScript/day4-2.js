//puzzle setup
const md5 = require('md5');
const input = "ckczppom";

var check = "";
var count = -1;

do {
    count++;
    check = input + String(count);
} while (md5(check).substring(0,6) !== "000000");
console.log(check);
