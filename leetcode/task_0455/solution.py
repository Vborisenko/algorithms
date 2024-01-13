from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0

        s.sort(reverse=True)
        g.sort(reverse=True)
        j = 0

        for i in range(len(g)):
            if i < len(g) and j < len(s):
                if g[i] <= s[j]:
                    j += 1
            else: break

        return j


if __name__ == '__main__':
    g = [1,2,3, 1,5,7,9]
    s = [1,1,2,3]

    result = Solution().findContentChildren(g, s)
    print(result)
