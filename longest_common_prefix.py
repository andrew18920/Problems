def longest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    strs.sort()
    a, b = strs[0], strs[-1]
    for i, ch in enumerate(a):
        if b[i] != ch:
            return a[:i]
    return a


def main():
    print(f"{longest_common_prefix(['flower','flow','flight']) = }")
    print(f"{longest_common_prefix(['dog','racecar','car']) = }")
    print(f"{longest_common_prefix(['glass','glare','glam']) = }")
    print(f"{longest_common_prefix(['']) = }")
    print(f"{longest_common_prefix(['','b']) = }")


if __name__ == "__main__":
    main()
