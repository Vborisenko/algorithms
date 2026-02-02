"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_map = dict()

        for i in range(len(nums)):
            if nums_map.get(nums[i]) is not None:
                if abs(nums_map[nums[i]] - i) <= k:
                    return True

            nums_map[nums[i]] = i

        return False
