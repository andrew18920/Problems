def pair_sum(a: list, k: int) -> list[tuple[int, int]]:
    k_diff = {}
    pairs = set()
    for item in a:
        k_diff[item] = k - item
        if k - item in k_diff:
            pairs.add((item, k - item))
    return pairs


def pair_diff(a: list, diff: int) -> list[tuple[int, int]]:
    item_diff = {}
    pairs = set()
    for item in a:
        item_diff[item] = item - diff
        if item - diff in item_diff:
            pairs.add((item, item - diff))
        if item + diff in item_diff:
            pairs.add((item, item + diff))
    return pairs


def main():
    print(f"{pair_sum([1, 2, 3, 4, 5, 0], 5) = }")
    print(f"{pair_diff([-1, 1, 3, 4, 5, 6, 4, 3, 10, 6], 3) = }")


if __name__ == "__main__":
    main()
