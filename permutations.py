def permutations_in_string(s: str, b: str) -> list[tuple]:
    found: list[tuple] = []
    i: int = 0
    while i < len(b) - len(s) + 1:
        ch: str = b[i]
        if ch in s:
            temp: list = list(s)
            temp.remove(ch)
            for c in range(1, 4):
                if b[i + c] in temp:
                    temp.remove(b[i + c])
                else:
                    break
            if not temp:
                found.append((i, i + 3))
        i += 1

    return found


def main():
    print(permutations_in_string("abbc", "cbabadcbbabbcbabaabccbabc"))


if __name__ == '__main__':
    main()
