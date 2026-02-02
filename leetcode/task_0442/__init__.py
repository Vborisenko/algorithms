"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n]
and each integer appears at most twice, return an array of all the integers that appears twice.

YOU MUST WRITE AN ALGORITHM THAT RUNS IN O(n) TIME AND USES ONLY CONSTANT AUXILIARY SPACE,
EXCLUDING THE SPACE NEEDED TO STORE THE OUTPUT
"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res