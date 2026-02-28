from collections import Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_counter = defaultdict(lambda: 0)
        p_keys_len = len(p_count.keys())
        filled_keys = set()
        result = []

        i = j = 0
        while j < len(s):
            if not p_count.get(s[j]):
                while i != j:
                    s_counter[s[i]] -= 1
                    if s[i] in filled_keys:
                        filled_keys.remove(s[i])
                    i += 1
                j += 1
                i += 1
                continue

            s_counter[s[j]] += 1

            if s_counter[s[j]] == p_count[s[j]]:
                filled_keys.add(s[j])
                if len(filled_keys) == p_keys_len:
                    result.append(i)
                    filled_keys.remove(s[i])
                    s_counter[s[i]] -= 1
                    i += 1

            while s_counter[s[j]] > p_count[s[j]]:
                s_counter[s[i]] -= 1
                if s[i] in filled_keys:
                    filled_keys.remove(s[i])
                i += 1

            j += 1

        return result


if __name__ == '__main__':
    s = "cbacebabacd"
    p = "abc"
    Solution().findAnagrams(s, p)
