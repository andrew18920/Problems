/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
*/

const maxArea = (height: number[]): number => {
  let [i, j] = [0, height.length - 1];
  let level = 0;
  while (i < j) {
    level = Math.max(level, (j - i) * Math.min(height[i], height[j]));
    if (height[i] < height[j]) {
      i += 1;
    } else {
      j -= 1;
    }
  }
  return level;
};

const run = [
  [1, 8, 6, 2, 5, 4, 8, 3, 7],
  [1, 1],
  [3, 4, 56, 1],
  [0, 1, 2, 0, 4, 1],
];

run.forEach((s) => {
  console.log(`maxArea([${s}]) = ${maxArea(s)}`);
});
