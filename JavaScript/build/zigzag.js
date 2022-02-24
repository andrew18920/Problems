/*
The string "PAYPALISHIRING" is written in a zigzag
pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
*/
const convert = (s, numRows) => {
    let i = 0;
    let step = numRows === 1 ? 0 : -1;
    const groups = new Array(numRows).fill('');
    [...s].forEach((char) => {
        groups[i] += char;
        if (i === 0 || i === numRows - 1) {
            step = -step;
        }
        i += step;
    });
    return groups.join('');
};
console.log(convert('PAYPALISHIRING', 3));
console.log(convert('PAYPALISHIRING', 4));
console.log(convert('A', 1));
