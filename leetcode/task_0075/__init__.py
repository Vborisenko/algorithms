"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.


Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        l => 0-value pointer fropm the beginning
        r => 2-value pointer from the end

        let's start from the l == 0, and r == len(nums) - 1 and move i from 1 to r.
        In case the i-th == 0, we have to switch nums[l] with nums[l] and increase l
        In case the i-th == 2, we have toi switch nums[i] with nums[r] and decrease
        """
        l = i = 0
        r = len(nums) - 1

        while i <= len(nums) - 1 and i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


if __name__ == '__main__':
    Solution().sortColors([0,1,0])