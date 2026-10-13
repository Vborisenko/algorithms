"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        target = nums[i] + nums[j] + nums[k] + m
        result = min(m)
        m = target - sum(nums[i], nums[j], nums[k])
        m_ = min(target - sum(nums[i], nums[j], nums[k]), current_min)

        [0, 1, 2, 3, ..., n]
        [-10, -5, -3, -1, 0, 0, 4, 5, 7, 10]
        """
        nums.sort()
        current_sum = current_min_diff = float("inf")
        for i in range(len(nums) - 2):
            if current_min_diff == target:
                return current_min_diff
            j = i + 1
            k = len(nums) - 1
            while j < k and current_sum != target:
                current_sum = nums[i] + nums[j] + nums[k]
                current_min_diff = current_sum if abs(target - current_sum) < abs(target - current_min_diff) else current_min_diff
                if target - current_sum > 0:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]: j += 1
                else:
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]: k -= 1

        return current_min_diff


if __name__ == '__main__':
    nums = [4,0,5,-5,3,3,0,-4,-5]
    Solution().threeSumClosest(nums, -2)
