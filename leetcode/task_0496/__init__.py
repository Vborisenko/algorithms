class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {}
        mon_stack = []
        for j in nums2:
            while mon_stack and mon_stack[-1] < j:
                nums2_map[mon_stack.pop()] = j
            mon_stack.append(j)

        return [nums2_map.get(i, -1) for i in nums1]
