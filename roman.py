value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s: str) -> int:
    prev = value_map[s[0]]
    total = prev
    for ch in s[1:]:
        total += value_map[ch]
        if prev < value_map[ch]:
            total -= prev * 2
        prev = value_map[ch]
    return total


def main():
    print(f"{romanToInt('III') = }")
    print(f"{romanToInt('IV') = }")
    print(f"{romanToInt('XIV') = }")
    print(f"{romanToInt('MMXXXI') = }")
    print(f"{romanToInt('MMCDXIII') = }")


if __name__ == "__main__":
    main()
