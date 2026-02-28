class Solution:
    @staticmethod
    def _is_pal(s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    @staticmethod
    def _check_s1_pref_s2_suff(s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        while l < r and s1[l] == s2[r]:
            l += 1
            r -= 1

        if l >= r:
            return True

        return Solution._is_pal(s1, l, r) or Solution._is_pal(s2, l, r)

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        res1 = self._check_s1_pref_s2_suff(a, b)
        return res1 if res1 else self._check_s1_pref_s2_suff(b, a)


if __name__ == '__main__':
    a ="pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    Solution().checkPalindromeFormation(a, b)