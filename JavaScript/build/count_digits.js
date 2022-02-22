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
    let out = '';
    groups.forEach((group) => {
        out += `${group.length}${group[0]}`;
    });
    return out;
};
['', '1', '3322251', '1234'].forEach((s) => {
    console.log(`countDigits(${s}) = ${countDigits(s)}`);
});
