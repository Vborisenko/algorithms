"""
2982. Find Longest Special Substring That Occurs Thrice II

You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
"""
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        Invariant:
        Firstly we have to find the longest substring of 1 symbol.
        The longest_length for such longest substring would be substring_length - 2 (Because we want to move our window 2 times more to get triple occuring)

        In case we'll find another substring of the same symbol (curr_subs_length) with curr_subs_length > current_max_length, the answer should be changed with the following rule:
        longest_length = curr_subs_length.
        Because longest_length + (curr_subs_length - longest_length) = curr_subs_length
        """

        l = r = 0
        special_s_map = defaultdict(lambda: [])

        while r < len(s):
            if s[r] == s[l]:
                r += 1
                continue
            else:
                special_s_map[s[l]].append(r - l)
                l = r

        special_s_map[s[l]].append(r - l)
        [special_s_map[k].sort() for k in special_s_map.keys()]
        max_length = 0

        for lengths in special_s_map.values():
            if len(lengths) > 1:
                current_max = lengths[-1] - 2 if lengths[-1] > 2 else 0 if len(lengths) == 2 and lengths[-1] < 2 else 1
                if current_max and current_max < lengths[-2]:
                    current_max += 1
                if  len(lengths) > 2 and current_max < lengths[-3]:
                    current_max += 1
            else:
                current_max = lengths[-1] - 2 if lengths[-1] > 2 else 0
            max_length = max(current_max, max_length)
        return max_length or -1


if __name__ == "__main__":
    s = "aada"
    s = "jicja"
    Solution().maximumLength(s)