from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def check_buckets(val):
            bucket = val // (valueDiff + 1)
            for b_ in range(bucket - 1, bucket + 2):
                possible = bucket_map.get(b_)
                if possible is not None:
                    if abs(possible - val) <= valueDiff:
                        return True
            return False

        bucket_map = {}
        j = 0
        for i in range(len(nums)):
            if i - j > indexDiff:
                bucket_ = nums[j] // (valueDiff + 1)
                bucket_map.pop(bucket_)
                j += 1
            if check_buckets(nums[i]):
                return True
            bucket_map[nums[i] // (valueDiff + 1)] = nums[i]
        return False


if __name__ == '__main__':
    nums = [0,5,0]
    valueDiff = 4
    indexDiff = 2
    Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)