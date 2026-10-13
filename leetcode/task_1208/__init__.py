class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        1) Build prefix sum for abs(t[i] - s[i])
        2) Find the logest subsequence of prefix_sum with sum() < maxCost
        """
        if len(s) != len(t):
            return 0

        prefix_sum = [0]
        for i in range(len(s)):
            prefix_sum.append(abs(ord(s[i]) - ord(t[i])) + prefix_sum[-1])

        j = result = 0
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] - prefix_sum[j] <= maxCost:
                result = max(result, i - j)
            else:
                while prefix_sum[i] - prefix_sum[j] > maxCost and j < i:
                    j += 1

        return result

if __name__ == '__main__':
    s = "anryddgaqpjdw"
    t = "zjhotgdlmadcf"
    cost = 5

    Solution().equalSubstring(s, t, cost)