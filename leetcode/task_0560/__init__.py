from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum_list = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum_list.append(prefix_sum_list[i-1] + nums[i])

        prefix_sum_list.append(0)

        for i in range(len(nums) + 1):
            j = i
            while j < len(nums):
                if prefix_sum_list[j] - prefix_sum_list[i-1] == k:
                    res +=1
                j += 1

        return res


if __name__ == '__main__':
    Solution().subarraySum([1,-1,0], 0)