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

[1234, 12, 0, 1927, 3049].forEach((s) => {
  console.log(`intToRoman(${s}) = ${intToRoman(s)}`);
});
