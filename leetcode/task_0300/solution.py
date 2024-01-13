from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    d[i] = max(d[i], d[j] + 1)

        return max(d)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))
