const pairSum = (a, k) => {
    const kDiff = {};
    const pairs = new Set();
    a.forEach((item) => {
        kDiff[item] = k - item;
        if (k - item in kDiff) {
            pairs.add([item, k - item]);
        }
    });
    return pairs;
};
const pairDiff = (a, diff) => {
    const itemDiff = {};
    const pairs = new Set();
    a.forEach((item) => {
        itemDiff[item] = item - diff;
        if (item - diff in itemDiff) {
            pairs.add(`${item}, ${item - diff}`);
        }
        if (item + diff in itemDiff) {
            pairs.add(`${item}, ${item + diff}`);
        }
    });
    return pairs;
};
console.log(pairSum([1, 2, 3, 4, 5, 0], 5));
console.log(pairDiff([-1, 1, 3, 4, 5, 6, 4, 3, 10, 6], 3));
