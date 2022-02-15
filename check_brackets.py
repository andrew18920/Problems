def check_brackets(s: str) -> bool:
    found = []
    for ch in s:
        expected = found[-1] if found else None
        if ch in "({[":
            found.append(ch)
        elif ch in ")}]":
            if found and (
                (ch == ")" and expected == "(")
                or (ch == "]" and expected == "[")
                or (ch == "}" and expected == "{")
            ):
                found.pop()
            else:
                return False
    return not found


def main():
    print(f"{check_brackets('()') = }")
    print(f"{check_brackets('[') = }")
    print(f"{check_brackets('()[]{}') = }")
    print(f"{check_brackets('(]') = }")
    print(f"{check_brackets('([)]') = }")


if __name__ == "__main__":
    main()
