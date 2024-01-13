from collections import defaultdict, Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count_map, t_count_map = Counter(s), Counter(t)
        difference = 0

        for letter, count in s_count_map.items():
            t_count = t_count_map.get(letter, 0)
            if t_count < count:
                difference += count - t_count

        return difference


if __name__ == '__main__':
    s, t = input().split()
    assert len(s) == len(t), 'Strings have a different length.'
    assert s.isalpha() and t.isalpha(), 'Strings do not contain only alpha characters.'

    Solution().minSteps(s, t)
