def isPalindrom(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    right = len(s) - 1
    left = 0
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    s = input()
    print(isPalindrom(s))


if __name__ == "__main__":
    main()