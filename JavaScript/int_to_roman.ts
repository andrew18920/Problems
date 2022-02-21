const intToRoman = (num: number): string => {
  let n = num;
  const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  const output: string[] = [];
  for (let i = 0; i < values.length; i += 1) {
    while (n >= values[i]) {
      output.push(letters[i]);
      n -= values[i];
    }
  }
  return output.join('');
};

const results = [
  `int_to_roman(1234) = '${intToRoman(1234)}'`,
  `int_to_roman(12) = '${intToRoman(12)}'`,
  `int_to_roman(0) = '${intToRoman(0)}'`,
  `int_to_roman(1927) = '${intToRoman(1927)}'`,
  `int_to_roman(3049) = '${intToRoman(3049)}'`,
];

results.forEach((s) => {
  console.log(s);
});
