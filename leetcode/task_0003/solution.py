"""

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len((s)):
            return 0

        i, j = 0, 1
        sub_s_set = {s[0]}
        max_length = len(sub_s_set)

        while j < len(s):
            if s[j] not in sub_s_set:
                sub_s_set.add(s[j])
            else:
                while s[j] in sub_s_set:
                    sub_s_set.remove(s[i])
                    i += 1
            max_length = max(max_length, len(sub_s_set))
            sub_s_set.add(s[j])
            j += 1
        return max_length



if __name__ == '__main__':
    s = "abcadbcbb"
    Solution().lengthOfLongestSubstring(s)
