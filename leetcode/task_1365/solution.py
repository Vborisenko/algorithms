"""
1365. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
"""
from collections import Counter


class Solution1:
    def smallerNumbersThanCurrent(self, nums):
        #prefix sum
        nums_counter = Counter(nums)
        prefix_sum = [0]

        for i in range(1, 101):
            prefix_sum.append(nums_counter.get(i - 1, 0) + prefix_sum[i - 1])

        return [prefix_sum[i] for i in nums]


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        nums_sum = sum(nums)
        nums_counter = Counter(nums)
        sum_map = {}
        sorted_keys = sorted(nums_counter.keys(), reverse=True)

        for num in sorted_keys:
            sum_map[num] = nums_sum - num * nums_counter[num]
            nums_sum = sum_map[num]

        return [sum_map[i] for i in nums]


if __name__ == '__main__':
    nums = []
    Solution().smallerNumbersThanCurrent(nums)

