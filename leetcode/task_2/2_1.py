# https://leetcode.com/problems/palindrome-number/submissions/
# 21.12.2021


def is_palindrome(x: int) -> bool:
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    print(is_palindrome(-11))
