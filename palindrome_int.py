def is_palindrome(x: int) -> bool:
    rev = 0
    n = x
    while x > 0:
        remainder = x % 10
        rev = rev * 10 + remainder
        x //= 10
    return rev == n


def main():
    print(f"{is_palindrome(121) = }")
    print(f"{is_palindrome(-121) = }")
    print(f"{is_palindrome(10) = }")
    print(f"{is_palindrome(101) = }")


if __name__ == "__main__":
    main()
