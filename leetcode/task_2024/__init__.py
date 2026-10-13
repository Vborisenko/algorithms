class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        def get_max_subs(ch):
            max_length = current_bad = l = r = 0
            n = len(s)
            while r < n:
                if s[r] != ch:
                    current_bad += 1
                    while current_bad > k and l < r:
                        if s[l] != ch:
                            current_bad -= 1
                        l += 1
                r += 1
                max_length = max(max_length, r - l)
            return max_length
        return max(get_max_subs("F"), get_max_subs("T"))
