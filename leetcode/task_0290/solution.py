class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split()) != len(pattern):
            return False

        s_map = {}

        for i in range(len(pattern)):
            if s_map.get(pattern[i]) is None:
                s_map[pattern[i]] = s.split()[i]
            else:
                if s_map[pattern[i]] != s.split()[i]:
                    return False

        return len(set(s_map.values())) == len(s_map.values())


if __name__ == '__main__':
    Solution().wordPattern(pattern="abba", s="dog cat cat dog")