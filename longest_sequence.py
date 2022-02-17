# longest alphabetical substring
def longest_sequence(s: str) -> tuple[str, int]:
    longest_str = s[0]
    curr_str = s[0]
    for i, ch in enumerate(s[1:]):
        if s[i] <= s[i + 1]:
            curr_str += s[i + 1]
        else:
            curr_str = s[i + 1]
        if len(curr_str) > len(longest_str):
            longest_str = curr_str

    return longest_str, len(longest_str)


def main():
    print(f"{longest_sequence('sample string') = }")
    print(f"{longest_sequence('sample stringabcdefghmza') = }")


if __name__ == "__main__":
    main()
