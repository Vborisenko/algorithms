from typing import List
import math

class Solution1:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Two pointers solution:
        We have  the current_min and  the current_max for actual valid window. current_min = current_max = nums[i] and max_length = 0
        Also we have i-th (right pointer) and j-th (left pointer) pointers for calculating the window.
        Let's loop through the array nums and follow the rules:

        1) On each iteration the difference between current_max and current_min should be less or eq. our limit.
        2) if our 1st condition is broken (nums[i] > current_max or nums[i] < current_min)
        we have to start externd our left boundary (j-th) with the following rule:
            a) if nums[i] > current_max:
                we have to move l-th while nums[i] - nums[j] with updating current_min on each step
                Also we have to update current_max with nums[i] at the end
            b) if nums[i] < current_min:
                we have to move l-th while nums[j] - nums[i] with updating current_max on each step
                Also we have to update current_min with nums[i] at the end
        3) Calculate the max_length on each step
        """
        current_max = current_min = nums[0]
        max_length = j = 0
        for i in range(len(nums)):
            if current_min <= nums[i] <= current_max:
                max_length = max(max_length, i - j + 1)
                continue
            if nums[i] > current_max:
                if nums[i] - current_min <= limit:
                    current_max = nums[i]
                else:
                    j = i
                    current_min = nums[j]
                    while nums[i] - nums[j - 1] <= limit:
                        j -= 1
                        current_min = min(current_min, nums[j])
                    current_max = nums[i]
            elif nums[i] < current_min:
                if current_max - nums[i] <= limit:
                    current_min = nums[i]
                else:
                    j = i
                    current_max = nums[j]
                    while nums[j - 1] - nums[i] <= limit:
                        j -= 1
                        current_max = max(nums[j], current_max)
                    current_min = nums[i]
            max_length = max(max_length, i - j + 1)
        return max_length


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        compressed_coordinates = {val: i for i, val in enumerate(sorted(list(set(nums))))}
        nums = [compressed_coordinates[i] for i in nums]
        freq = []

        for i in range(len(nums)):
            ...

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # 1) Coordinate compression
        values = sorted(set(nums))                 # real values sorted
        M = len(values)
        index = {v: i for i, v in enumerate(values)}  # real value -> compressed idx
        comp = [index[x] for x in nums]            # nums in compressed coords

        # 2) Buckets setup
        B = int(math.isqrt(M)) + 1                 # bucket size
        num_buckets = (M + B - 1) // B

        freq = [0] * M
        bucket_count = [0] * num_buckets

        def add(idx: int) -> None:
            freq[idx] += 1
            bucket_count[idx // B] += 1

        def remove(idx: int) -> None:
            freq[idx] -= 1
            bucket_count[idx // B] -= 1

        def get_min_idx() -> int:
            # Find first non-empty bucket
            for b in range(num_buckets):
                if bucket_count[b] > 0:
                    start = b * B
                    end = min(M, start + B)
                    for i in range(start, end):
                        if freq[i] > 0:
                            return i
            return -1  # should not happen if window non-empty

        def get_max_idx() -> int:
            # Find last non-empty bucket
            for b in range(num_buckets - 1, -1, -1):
                if bucket_count[b] > 0:
                    start = b * B
                    end = min(M, start + B)
                    for i in range(end - 1, start - 1, -1):
                        if freq[i] > 0:
                            return i
            return -1  # should not happen if window non-empty

        left = 0
        best = 0

        for right in range(n):
            add(comp[right])

            # shrink while invalid
            while True:
                min_i = get_min_idx()
                max_i = get_max_idx()
                if values[max_i] - values[min_i] <= limit:
                    break
                remove(comp[left])
                left += 1

            best = max(best, right - left + 1)

        return best






if __name__ == '__main__':
    nums =  [8, 2, 4, 7, 2, 10, 4]
    limit = 6
    Solution().longestSubarray(nums, limit)