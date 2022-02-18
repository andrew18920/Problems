def picking_numbers(a: list[int]) -> int:
    # Longest sublist for which diff between any two elements <= 1
    # min(x) - max(x) <= 1
    max = 0
    for i in a:
        count_i, count_below = a.count(i), a.count(i-1)
        curr = count_i + count_below
        if curr > max:
            max = curr
    return max


def main():
    print(picking_numbers([10, 10, 10, 10, 4, 4, 3, 2, 2, 9, 9, 9, 8]))


if __name__ == "__main__":
    main()
