from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list({_ for _ in range(1, len(nums)+1)}.difference(set(nums)))


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_map, res = {}, []
        for i in nums:
            if nums_map.get(i) is not None:
                nums_map[i] += 1
            else:
                nums_map[i] = 1

        for i in range(1, len(nums) + 1):
            if not nums_map.get(i):
                res.append(i)

        return res


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1

        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

if __name__ == '__main__':
    Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
