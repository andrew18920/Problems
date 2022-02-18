var pair_sum = function (a, k) {
    k_diff = {}
    pairs = new Set();
    a.forEach(item => {
        k_diff[item] = k - item;
        if (k - item in k_diff) {
            pairs.add([item, k - item]);
        }
    });
    return pairs;
};

console.log(pair_sum([1, 2, 3, 4, 5, 0], 5))