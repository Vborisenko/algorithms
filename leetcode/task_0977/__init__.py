class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [i ** 2 for i in nums]

        if nums[-1] <= 0:
            nums.reverse()
            return [i ** 2 for i in nums]

        res = []
        l = 0
        r = l - 1
        while (-r + l + 1) <= len(nums) + 1:
            if nums[r] ** 2 >= nums[l] ** 2:
                res.insert(0, nums[r] ** 2)
                r -= 1
            else:
                res.insert(0, nums[l] ** 2)
                l += 1

        return res

