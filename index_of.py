def index_of(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(0, len(haystack) + len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1


def main():
    print(f"{index_of('a','a') = }")
    print(f"{index_of('apple','a') = }")
    print(f"{index_of('hello','ll') = }")
    print(f"{index_of('mississippi', 'issipi') = }")
    print(f"{index_of('mississippi', 'issip') = }")


if __name__ == "__main__":
    main()
