var int_to_roman = function (num) {
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];

    var output = [];
    for (let i = 0; i < values.length; i++) {
        while (num >= values[i]) {
            output.push(letters[i]);
            num -= values[i];
        }
    }
    return output.join("");
}

results = [
    `int_to_roman(1234) = '${int_to_roman(1234)}'`,
    `int_to_roman(12) = '${int_to_roman(12)}'`,
    `int_to_roman(0) = '${int_to_roman(0)}'`,
    `int_to_roman(1927) = '${int_to_roman(1927)}'`,
    `int_to_roman(3049) = '${int_to_roman(3049)}'`,
]

results.forEach(s => {
    console.log(s);
});