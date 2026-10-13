from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = l = r = 0
        min_length = float('inf')
        while r < len(nums):
            current_sum += nums[r]
            while l <= r and current_sum >= target:
                if current_sum >= target:
                    min_length = min(r - l + 1, min_length)
                current_sum -= nums[l]
                l += 1
            r += 1
        return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    nums = [1,4,4]
    target = 4
    Solution().minSubArrayLen(target, nums)