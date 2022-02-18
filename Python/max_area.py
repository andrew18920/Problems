"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""


def max_area(height: list[int]) -> int:
    # start v end, if start < end: increment start. if end < start: decrement end
    i, j = 0, len(height) - 1
    level = 0
    while i < j:
        level = max(level, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return level


def main():
    print(f"{max_area([1,8,6,2,5,4,8,3,7]) = }")
    print(f"{max_area([1,1]) = }")


if __name__ == "__main__":
    main()
