# https://leetcode.com/problems/two-sum/
# 21.12.2021
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    if sum(nums) == target and len(nums) == 2:
        return [x for x in range(len(nums))]
    for x in range(len(nums)):
        index1 = x

        try:
            index2 = nums.index(target-nums[x]) if nums.index(target-nums[x]) != index1 \
                else nums.index(target-nums[x], index1+1)

            if index2 != index1:
                return [index1, index2]
        except:
            continue

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_map = {}

        for i in range(len(nums)):
            if target - nums[i] in sub_map.keys():
                return [sub_map[target - nums[i]], i]

            sub_map[nums[i]] = i


if __name__ == '__main__':
    print(two_sum([0, 3, 2, 0], 0))
