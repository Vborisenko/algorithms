from typing import List


class Solution:
    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            center = (right+left) // 2

            if nums[center] == target:
                return center
            elif target > nums[center]:
                left = center + 1
            else:
                right = center - 1

        return center + 1 if nums[center] < target else center


if __name__ == '__main__':
    print(Solution.searchInsert([1, 1, 2, 5, 6], 3))
