inmin = "277799".split('');
inmax = 799999;
ans = [];
ct = 0;
valid = true;

check = Number(inmin.join('')) <= inmax;
do {
    for (let i = 5; i >= 0; i--)
    {
        if (valid === false) continue;
        if (i !== 0 && inmin[i] < inmin[i-1])
        {
            valid = false;
            continue;
        }
        if (i === 0 && valid && inmin.join('').match(/(\d)\1/g) && inmin.join('').match(/(\d)\1/g).length > 0)
        {
            ct++;
            ans.push(inmin.join(''));
        }
    }
    inmin = String((Number(inmin.join('')) + 1)).split('');
    check = Number(inmin.join('')) <= inmax;
    valid = true;
    doubles = false;
    doublect = 0;
} while (check)
console.log(ct);
console.log(ans);
