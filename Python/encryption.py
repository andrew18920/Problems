from math import ceil, sqrt
import timeit


def encryption(s: str) -> str:
    s = "".join(s.split(" "))
    col_len = ceil(sqrt(len(s)))
    cols = [[] for _ in range(col_len)]
    for i, ch in enumerate(s):
        cols[i % col_len].append(ch)

    cols = ["".join(li) for li in cols]
    return " ".join(cols)


def main():
    print(f"{encryption('have a nice day') = }")
    print(f"{encryption('feed the dog      ') = }")
    print(f"{encryption('chill out') = }")
    print(
        f"{encryption('if man was meant to stay on the ground god would have given us roots') = }"
    )
    print(
        "encryption('haveaniceday') =",
        max(
            timeit.repeat(
                stmt="encryption('haveaniceday')",
                setup="from __main__ import encryption",
                number=100_000,
            )
        ),
    )


if __name__ == "__main__":
    main()
