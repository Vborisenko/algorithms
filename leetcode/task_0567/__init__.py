"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        1) Permutations of s1 could be a substring of s2, if counter(s1) == counter(sub_s2)
        2) We can move the right pointer (j-th) till counter_1[s[j]] <= counter_s[s[j]], on the other hand we can move left(i-th)
        """
        if s1 == s2:
            return True
        elif len(s2) == 1 or len(s2) <= len(s1):
            False

        counter_s1 = {}

        for i in s1:
            if counter_s1.get(i, 0):
                counter_s1[i] += 1
            else:
                counter_s1[i] = 1

        i, j = 0, 1
        counter_s2 = {s2[i]: 1}

        if counter_s1 == counter_s2:
            return True

        while j < len(s2):
            if counter_s2.get(s2[j], 0):
                counter_s2[s2[j]] += 1
            else:
                counter_s2[s2[j]] = 1

            if s2[j] in counter_s1:
                while s2[i] not in counter_s1 or counter_s2[s2[i]] > counter_s1[s2[i]]:
                    counter_s2[s2[i]] -= 1
                    if counter_s2.get(s2[i], 0) == 0:
                        counter_s2.pop(s2[i], 0)
                    i += 1
            j += 1
            if counter_s1 == counter_s2:
                return True
        return False

if __name__ == '__main__':
    s1 = "adc"
    s2 = "dcda"
    Solution().checkInclusion(s1, s2)