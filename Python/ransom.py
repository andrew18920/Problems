# Can a ransom note (string) be formed from a given magazine (string)
from collections import Counter


def ransom_possible(ransom: str, magazine: str) -> bool:
    ransom_counter = Counter(ransom)
    magazine_counter = Counter(magazine)
    for ch, freq in ransom_counter.items():
        if ch not in magazine_counter or magazine_counter[ch] < freq:
            return False
    return True


def main():
    print(ransom_possible("hexllo", "elloh pycharm"))


if __name__ == '__main__':
    main()
