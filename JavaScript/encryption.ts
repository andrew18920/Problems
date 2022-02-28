const encryption = (s: string) => {
  const s1 = s.replace(/\s+/g, '');
  const colLength = Math.ceil(Math.sqrt(s1.length));
  const columns = new Array(colLength).fill('');

  for (let i = 0; i < s1.length; i += 1) {
    columns[i % colLength] += s1[i];
  }

  return columns.join(' ');
};

[
  'have a nice day',
  'feed the dog      ',
  'chill out',
  'if man was meant to stay on the ground god would have given us roots',
].forEach((s) => {
  console.log(`encryption('${s}') = '${encryption(s)}'`);
});
