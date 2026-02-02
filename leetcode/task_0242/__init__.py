from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def calculate_letters(str_: str) -> dict:
            res_map = defaultdict(lambda: 0)
            for l in str_:
                res_map[l] += 1
            return res_map

        s_map, t_map = calculate_letters(s), calculate_letters(t)

        for key in s_map.keys():
            if s_map[key] != t_map.pop(key, None):
                return False

        return True if not t_map.keys() else False


if __name__ == '__main__':
    Solution().isAnagram("anagram", "nagaram")