const pairSum = (a: number[], k: number): Set<number[]> => {
  const kDiff = new Map<number, number>();
  const pairs = new Set<number[]>();
  a.forEach((item) => {
    kDiff.set(item, k - item);
    if (kDiff.has(k - item)) {
      pairs.add([item, k - item]);
    }
  });
  return pairs;
};

const pairDiff = (a: number[], diff: number): Set<string> => {
  const itemDiff = new Map<number, number>();
  const pairs = new Set<string>();
  a.forEach((item) => {
    itemDiff.set(item, item - diff);
    if (itemDiff.has(item - diff)) {
      pairs.add(`${item}, ${item - diff}`);
    }
    if (itemDiff.has(item + diff)) {
      pairs.add(`${item}, ${item + diff}`);
    }
  });
  return pairs;
};

console.log(pairSum([1, 2, 3, 4, 5, 0], 5));
console.log(pairDiff([-1, 1, 3, 4, 5, 6, 4, 3, 10, 6], 3));
