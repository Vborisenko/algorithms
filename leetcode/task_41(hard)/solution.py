class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = set(nums)
        smallest_positive_integer = 1
        nums_length = len(nums)

        while nums_length:
            if smallest_positive_integer not in nums:
                return smallest_positive_integer

            smallest_positive_integer += 1
            nums_length -= 1

        return smallest_positive_integer
