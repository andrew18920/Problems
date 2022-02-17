"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""


def max_area(height: list[int]) -> int:
    # brute force
    max_area = 0
    for i, a in enumerate(height):
        for j, b in enumerate(height[i + 1 :]):
            area = min(a, b) * (j + 1)
            if area > max_area:
                max_area = area
    return max_area


def main():
    print(f"{max_area([1,8,6,2,5,4,8,3,7]) = }")


if __name__ == "__main__":
    main()
