"""
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.


Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
"""


def remove_covered_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: (x[0], -x[1]))
    print(intervals)

    count = 1
    prevRight = intervals[0][1]
    for _, right in intervals[1:]:
        if prevRight < right:
            count += 1
            prevRight = right
    return count


def main():
    print(f"{remove_covered_intervals([[1,4],[3,6],[2,8]]) = }")
    print(f"{remove_covered_intervals([[1,4],[2,3]]) = }")


if __name__ == "__main__":
    main()
