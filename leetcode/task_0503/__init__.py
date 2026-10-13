class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        results = [-1] * len(nums)
        n = len(nums)
        mon_stack = []

        for i in range(n * 2):
            idx = i % n
            while mon_stack and nums[mon_stack[-1]] < nums[idx]:
                j = mon_stack.pop()
                results[j] = nums[idx]
            if i < n:
                mon_stack.append(i)

        return results