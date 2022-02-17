"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""


def convert(s: str, numRows: int) -> str:
    i = 0
    step = (numRows == 1) - 1
    groups = [[] for _ in range(numRows)]

    for ch in s:
        groups[i].append(ch)
        if i in (0, numRows - 1):
            step = -step
        i += step

    return "".join("".join(row) for row in groups)


def main():
    print(f"{convert('PAYPALISHIRING', 3) = }")
    print(f"{convert('PAYPALISHIRING', 4) = }")
    print(f"{convert('A', 1) = }")


if __name__ == "__main__":
    main()
