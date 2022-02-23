/*
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.


Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
*/

const removeCoveredIntervals = (intervals: number[][]): number => {
  intervals.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

  let count = 1;
  let prevRight = intervals[0][1];
  intervals.slice(1).forEach((interval) => {
    const right = interval[1];
    if (prevRight < right) {
      count += 1;
      prevRight = right;
    }
  });
  return count;
};

[
  [
    [1, 4],
    [3, 6],
    [2, 8],
  ],
  [
    [1, 4],
    [2, 3],
  ],
].forEach((s) => {
  console.log(`removeCoveredIntervals([${JSON.stringify(s)}]) = ${removeCoveredIntervals(s)}`);
});
