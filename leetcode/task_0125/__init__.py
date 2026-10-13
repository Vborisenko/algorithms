class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([_ for _ in s if _.isalpha() or _.isdigit()]).lower()

        if len(s) == 0:
            return True

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1

        return True
