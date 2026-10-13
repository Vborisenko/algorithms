class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        We have 2 pointers L-th and R-th, and the current admissible counter of the 0 in the L:R window (zero_counter).
        Iterate for the nums array. On each step increment the r-th pointer.
        In case of r-th element is 0, zero_counter should be increased. If  zero_counter == k, then we have to move l for the first i-th + 1 element
        where nums[i] == 0. Each loop step max_length should be updates.
        """
        r = l = zero_counter = max_length = 0
        while r < len(nums):
            if nums[r] is 0:
                zero_counter += 1
            while l <= r and zero_counter > k:
                if nums[l] == 0:
                    zero_counter -= 1
                l += 1
            max_length = max(max_length, r - l +1)
            r += 1
        return max_length
