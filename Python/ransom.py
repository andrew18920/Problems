# Can a ransom note (string) be formed from a given magazine (string)
from collections import Counter


def ransom_possible(ransom: str, magazine: str) -> bool:
    ransom_counter = Counter(ransom)
    magazine_counter = Counter(magazine)
    return not any(
        ch not in magazine_counter or magazine_counter[ch] < freq
        for ch, freq in ransom_counter.items()
    )


def main():
    print(ransom_possible("hexllo", "elloh pycharm"))


if __name__ == "__main__":
    main()
