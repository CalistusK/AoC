//puzzle setup
const fs = require('fs');
var input = "";
const phaseMax = 100;

var input = fs.readFileSync('../day16in.txt', 'utf8');
var parsed = input.split('');
//console.log(arr);

//do stuff?
var pattern = [];
var phaseCurr = 1;
var phaseHolder = [];
var temp = 0;
var phaseIdx = 1;
var debugCount = 0;

for (let i = 0; i < 100; i++)
{
    debugCount = i;
    phaser(parsed);
}

function phaser(arr)
{
    arr = [...arr];
    for (let i = 0; i < arr.length; i++)
    {
        makePattern(i+1);
        for (let j = 0; j < arr.length; j++)
        {
            temp += pattern[phaseIdx] * arr[j];
            phaseIdx++;
            if (phaseIdx === pattern.length) phaseIdx = 0;
        }
        if (String(temp).length >= 2) temp = Math.abs(temp) % 10;
        phaseHolder.push(temp);
        temp = 0;
        phaseIdx = 1;
        pattern = [];
        //console.log(phaseHolder);
    }
    parsed = phaseHolder;
    phaseHolder = [];
    /*if (debugCount == 99) */console.log("iteration " + debugCount + ": " + parsed.join(''));
}

function makePattern(times)
{
    for (let i = 0; i < times; i++) pattern.push(0);
    for (let i = 0; i < times; i++) pattern.push(1);
    for (let i = 0; i < times; i++) pattern.push(0);
    for (let i = 0; i < times; i++) pattern.push(-1);
}
