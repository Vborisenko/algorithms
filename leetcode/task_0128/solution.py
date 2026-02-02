"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
"""
from typing import List


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        current_max = 0

        for i in nums:
            if i-1 not in nums:
                j = i
                while j in nums:
                    currentcurrent_length = j-i+1
                    current_max = currentcurrent_length if currentcurrent_length > current_max else current_max
                    j += 1

        return current_max


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        current_max = 0

        for i in nums:
            if i-1 not in nums:
                j = i
                while j in nums:
                    j += 1

                current_max = j-i if j-i > current_max else current_max

        return current_max


if __name__ == "__main__":
    ...
