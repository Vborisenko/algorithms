from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        1st step is to find a first shortest substrings with at least one occurrence of all these characters.
        (We should iterate through s with 2 pointers (l = 0, r should be increased) and count each ch until all.
        Then we can move l with decreasing s[l], until freq_map[s[l]] == 1).

        At this step is our subs_count is l + 1 + (len(s) - r - 1) = len(s) - r + l

        2nd step is to move
        """
        freq_map = defaultdict(lambda: 0)
        result = l = 0
        length = len(s)

        for r in range(len(s)):
            freq_map[s[r]] += 1
            if len(freq_map.keys()) == 3:
                result += length - r

                while freq_map[s[l]] != 1:
                    result += 1
                    freq_map[s[l]] -= 1
                    l += 1

                freq_map.pop(s[l])
                l += 1

        return result


if __name__ == '__main__':
    s = "acbbcac"
    Solution().numberOfSubstrings(s)
