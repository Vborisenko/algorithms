"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

from collections import Counter
from heapq import heapify, heappop


# sorted
class Solution1:
    def frequencySort(self, s: str) -> str:
        return ''.join(
            sorted(
                [key * value for key, value in Counter(list(s)).items()],
                key=lambda x: len(x), reverse=True
            )
        )

# Heap approach
class Solution:
    def frequencySort(self, s: str) -> str:
        s_heap = [(-count, letter) for letter, count in Counter(s).items()]
        heapify(s_heap)
        res = ""

        for _ in range(len(s_heap)):
            count, letter = heappop(s_heap)
            res += -count*letter

        return res


if __name__ == '__main__':
    Solution().frequencySort("cccaaareacadcassa")
