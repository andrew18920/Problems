const pairSum = (a, k) => {
    const kDiff = new Map();
    const pairs = new Set();
    a.forEach((item) => {
        kDiff.set(item, k - item);
        if (kDiff.has(k - item)) {
            pairs.add([item, k - item]);
        }
    });
    return pairs;
};
const pairDiff = (a, diff) => {
    const itemDiff = new Map();
    const pairs = new Set();
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
