def check_brackets(s: str) -> bool:
    brackets = {"]": "[", "}": "{", ")": "(", ">": "<"}
    found = []
    for ch in s:
        if ch in brackets.values():
            found.append(ch)
        elif ch in brackets:
            if not found or brackets[ch] != found.pop():
                return False
        else:
            return False
    return not found


def main():
    print(f"{check_brackets('<()>') = }")
    print(f"{check_brackets('[') = }")
    print(f"{check_brackets('()[]{}<>') = }")
    print(f"{check_brackets('(]') = }")
    print(f"{check_brackets('([)]') = }")


if __name__ == "__main__":
    main()
