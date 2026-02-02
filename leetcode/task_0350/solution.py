class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        map_ = {}

        for i in range(len(nums2)):
            if map_.get(nums2[i]) is not None:
                map_[nums2[i]] += 1
            else:
                map_[nums2[i]] = 1

        res = []

        for i in range(len(nums1)):
            if map_.get(nums1[i]):
                res.append(nums1[i])
                map_[nums1[i]] -= 1

        return res
