from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Block decomposition

        The main idea is to split the array nums for blocks with k elements.
        E.g.:
        nums [1,3,-1,-3,5,3,6,7]
        [1,3,-1]
        [-3,5,3]
        [6,7]

        Then we want to build 2 arrays: left_max and right_max with length nums.
        In left_max for each i-th we want to store max(nums[i], nums[i - 1]) in each block.
        In right_max we do the same, but the only difference is in indeces: max(nums[j], nums[j + 1]) in each block.

        Then we can iterate for nums indeces in range [0 : len(nums) - k + 1] (because )


        [ -7,-8,7,5, 7,1,6,0 ]

        [-7, -7, 7, 7, 7, 7, 7, 7]
        [7, 7, 7, 5, 7, 6, 6, 0]

        [7, 7, 7, ]
        """
        left_max = []
        right_max = []
        n = len(nums)
        for i in range(n):
            if i % k == 0:
                left_max.append(nums[i])
            else:
                left_max.append(max(nums[i], left_max[i - 1]))
            j = n - i - 1
            if (j + 1) % k == 0 or j == n - 1:
                right_max.insert(0, nums[j])
            else:
                right_max.insert(0, max(nums[j], right_max[0]))
        return [max(right_max[i], left_max[i + k - 1]) for i in range(n - k + 1)]


if __name__ == '__main__':
    nums =[-7,-8,7,5,7,1,6,0]
    k = 4
    Solution().maxSlidingWindow(nums, k)