class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        max_length = 1
        r = 1
        first_pair_index = None

        while r <= len(s) - 1:
            if s[r] == s[r - 1] and not first_pair_index:
                first_pair_index = r
            elif s[r] == s[r - 1] and first_pair_index:

                l = first_pair_index
                first_pair_index = r
            max_length = max(r - l + 1, max_length)
            r += 1

        return max_length


if __name__ == '__main__':
    s = "0001"
    Solution().longestSemiRepetitiveSubstring(s)