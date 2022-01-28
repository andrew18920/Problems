def longest_sequence(s):
    longest_str = s[0]
    curr_str = s[0]
    for i, ch in enumerate(s[1:]):
        if s[i] <= s[i+1]:
            curr_str += s[i+1]
        else:
            curr_str = s[i+1]
        if len(curr_str) > len(longest_str):
            longest_str = curr_str

    return longest_str, len(longest_str)


print(longest_sequence('sample string'))
