from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[k] == nums[k - 1] and k > j:
                        k -= 1
                    while nums[j] == nums[j + 1] and j < k:
                        j += 1
                    continue
                if nums[i] + nums[j] + nums[k] >= 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return result


if __name__ == '__main__':
    nums = [1,2,0,1,0,0,0,0]
    Solution().threeSum(nums)
