def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0
    longest = [s[0]]
    curr_substr = longest
    for ch in s[1:]:
        if ch in curr_substr:
            chIndex = curr_substr.index(ch)
            curr_substr = curr_substr[chIndex + 1 :]
        curr_substr.append(ch)

        if len(curr_substr) > len(longest):
            longest = curr_substr
    return len(longest)


def main():
    print(f"{length_of_longest_substring('abcabcbb') = }")
    print(f"{length_of_longest_substring('bbbbb') = }")
    print(f"{length_of_longest_substring('pwwkew') = }")
    print(f"{length_of_longest_substring('dvdf') = }")


if __name__ == "__main__":
    main()
