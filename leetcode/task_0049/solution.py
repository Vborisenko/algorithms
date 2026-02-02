"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return strs

        res = defaultdict(lambda: [])
        for s in strs:
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)

        return list(res.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Solution().groupAnagrams(strs)
