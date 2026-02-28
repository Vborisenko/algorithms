from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        left_freq_map = defaultdict(lambda: 0)
        right_freq_map = defaultdict(lambda: 0)
        for i in s: right_freq_map[i] += 1
        r_count = len(right_freq_map.keys())
        result = l_count = 0

        for ch in s[:-1]:
            if left_freq_map[ch] == 0:
                l_count += 1
            if right_freq_map[ch] == 0:
                r_count -= 1

            left_freq_map[ch] += 1
            right_freq_map[ch] -= 1

            if r_count == l_count:
                result += 1

        return result



if __name__ == '__main__':
    s = "aacaba"
    Solution().numSplits(s)
