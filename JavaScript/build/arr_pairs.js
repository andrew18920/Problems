var pair_sum = (a, k) => {
    let k_diff = {};
    let pairs = new Set();
    a.forEach(item => {
        k_diff[item] = k - item;
        if (k - item in k_diff) {
            pairs.add([item, k - item]);
        }
    });
    return pairs;
};
var pair_diff = (a, diff) => {
    let item_diff = {};
    let pairs = new Set();
    a.forEach(item => {
        item_diff[item] = item - diff;
        if (item - diff in item_diff) {
            pairs.add(`${item}, ${item - diff}`);
        }
        ;
        if (item + diff in item_diff) {
            pairs.add(`${item}, ${item + diff}`);
        }
        ;
    });
    return pairs;
};
console.log(pair_sum([1, 2, 3, 4, 5, 0], 5));
console.log(pair_diff([-1, 1, 3, 4, 5, 6, 4, 3, 10, 6], 3));
