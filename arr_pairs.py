def pair_sum(a: list, k: int) -> list:
    hashmap = {}
    pairs = set()
    for item in a:
        hashmap[item] = k - item
        if k - item in hashmap:
            pairs.add((item, k-item))
    return pairs


def main():
    print(pair_sum([1, 2, 3, 4, 5, 0], 5))


if __name__ == "__main__":
    main()
