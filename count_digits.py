# group digits and count them, output like: 'two 3s, three 2s, one 5, one 1s' (23321511)
def count_digits(n: str) -> str:
    prev = n[0]
    groups = []
    curr_group = [prev]
    for digit in n[1:]:
        if digit == prev:
            curr_group.append(digit)
        else:
            groups.append(curr_group)
            curr_group = [digit]
        prev = digit
    groups.append(curr_group)
    return "".join([f"{len(group)}{group[0]}" for group in groups])


def main():
    print(f"{count_digits('3322251') = }")
    print(f"{count_digits('1234') = }")
    print(f"{count_digits('8'*50+'3'*32) = }")


if __name__ == "__main__":
    main()
