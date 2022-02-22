const countDigits = (n) => {
    if (n === '') {
        return '';
    }
    let prev = n[0];
    const groups = [];
    let currGroup = [prev];
    [...n].slice(1).forEach((digit) => {
        if (digit === prev) {
            currGroup.push(digit);
        }
        else {
            groups.push(currGroup);
            currGroup = [digit];
        }
        prev = digit;
    });
    groups.push(currGroup);
    const out = [];
    groups.forEach((group) => {
        out.push(`${group.length}${group[0]}`);
    });
    return out.join('');
};
['', '1', '3322251', '1234'].forEach((s) => {
    console.log(`countDigits(${s}) = ${countDigits(s)}`);
});
